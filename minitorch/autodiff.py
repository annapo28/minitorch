from dataclasses import dataclass
from typing import Any, Iterable, List, Tuple

from typing_extensions import Protocol

# ## Task 1.1
# Central Difference calculation


def central_difference(f: Any, *vals: Any, arg: int = 0, epsilon: float = 1e-6) -> Any:
    r"""
    Computes an approximation to the derivative of `f` with respect to one arg.

    See :doc:`derivative` or https://en.wikipedia.org/wiki/Finite_difference for more details.

    Args:%%writefile /kaggle/working/train_fast.py
    train_dataset.tensors = (train_dataset.tensors[0], (train_dataset.tensors[1] - Y_mean) / Y_std)

    model = Trompt(n_columns=train_dataset.tensors[0].shape[1], n_prompts=128, d_model=128, n_cycles=6).to(device)
    model = nn.parallel.DistributedDataParallel(model, device_ids=[local_rank])
    model_c = torch.compile(model, mode="reduce-overhead")

    BATCH_SIZE = 1024  

    train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset, shuffle=True)
    train_dl = torch.utils.data.DataLoader(
        train_dataset, sampler=train_sampler, num_workers=4, batch_size=BATCH_SIZE,
        pin_memory=True, drop_last=True, persistent_workers=True, prefetch_factor=4,
    )
    val_dl = torch.utils.data.DataLoader(val_dataset, num_workers=2, batch_size=2048, pin_memory=True)

    optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4, weight_decay=1e-5)
    scaler = torch.amp.GradScaler('cuda') 
    Y_mean, Y_std = Y_mean.to(device), Y_std.to(device)
    EPOCHS = 5

    for e in range(1, EPOCHS + 1):
        model.train()
        train_sampler.set_epoch(e)

        n_samples = 0
        torch.cuda.synchronize()
        t0 = time.perf_counter()
        for x, y in tqdm(train_dl, disable=(rank != 0)):
            x = x.to(device, non_blocking=True)
            y = y.to(device, non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast(device_type='cuda', dtype=torch.float16):
                pred = model_c(x)
                loss = F.mse_loss(pred, y.unsqueeze(1).expand(-1, pred.shape[1]))
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()
            n_samples += x.shape[0]
        torch.cuda.synchronize()
        elapsed = time.perf_counter() - t0

        stats = torch.tensor([float(n_samples), elapsed], device=device)
        dist.all_reduce(stats[0:1], op=dist.ReduceOp.SUM)
        dist.all_reduce(stats[1:2], op=dist.ReduceOp.MAX)
        samples_per_sec = stats[0].item() / stats[1].item()

        model.eval()
        mae = torch.zeros((), device=device)
        with torch.inference_mode():
            for x, y in val_dl:
                x = x.to(device, non_blocking=True)
                y = y.to(device, non_blocking=True)
                with torch.autocast(device_type='cuda', dtype=torch.float16):
                    pred = model_c(x)
                mae += (pred.float().mean(dim=-1) * Y_std + Y_mean - y).abs().sum()

        mae = (mae / len(val_dataset)).item() 
        if rank == 0:
            print(f'>>> Epoch {e:>02}')
            print(f'Throughput = {samples_per_sec:.1f} samples/sec' + (' (includes torch.compile warmup)' if e == 1 else ''))
            print(f'Validation MAE = {mae:.5f}')
            print('>>>\n')

    dist.destroy_process_group()


if __name__ == "__main__":
    main()
        f : arbitrary function from n-scalar args to one value
        *vals : n-float values $x_0 \ldots x_{n-1}$
        arg : the number $i$ of the arg to compute the derivative
        epsilon : a small constant

    Returns:
        An approximation of $f'_i(x_0, \ldots, x_{n-1})$
    """
    vals1 = list(vals)
    vals2 = list(vals)
    vals1[arg] += epsilon
    vals2[arg] -= epsilon
    return (f(*vals1) - f(*vals2)) / (2 * epsilon)


variable_count = 1


class Variable(Protocol):
    def accumulate_derivative(self, x: Any) -> None:
        pass

    @property
    def unique_id(self) -> int:
        pass

    def is_leaf(self) -> bool:
        pass

    def is_constant(self) -> bool:
        pass

    @property
    def parents(self) -> Iterable["Variable"]:
        pass

    def chain_rule(self, d_output: Any) -> Iterable[Tuple["Variable", Any]]:
        pass


def topological_sort(variable: Variable) -> Iterable[Variable]:
    """
    Computes the topological order of the computation graph.

    Args:
        variable: The right-most variable

    Returns:
        Non-constant Variables in topological order starting from the right.
    """
    order: List[Variable] = []
    seen = set()

    def visit(var: Variable) -> None:
        if var.unique_id in seen or var.is_constant():
            return
        if not var.is_leaf():
            for parent in var.parents:
                visit(parent)
        seen.add(var.unique_id)
        order.insert(0, var)

    visit(variable)
    return order


def backpropagate(variable: Variable, deriv: Any) -> None:
    """
    Runs backpropagation on the computation graph in order to
    compute derivatives for the leave nodes.

    Args:
        variable: The right-most variable
        deriv  : Its derivative that we want to propagate backward to the leaves.

    No return. Should write to its results to the derivative values of each leaf through `accumulate_derivative`.
    """
    order = topological_sort(variable)
    derivatives = {variable.unique_id: deriv}

    for var in order:
        d_output = derivatives[var.unique_id]
        if var.is_leaf():
            var.accumulate_derivative(d_output)
        else:
            for parent, d_in in var.chain_rule(d_output):
                if parent.is_constant():
                    continue
                if parent.unique_id in derivatives:
                    derivatives[parent.unique_id] += d_in
                else:
                    derivatives[parent.unique_id] = d_in

def backpropagate(variable: Variable, deriv: Any) -> None:
    """
    Runs backpropagation on the computation graph in order to
    compute derivatives for the leave nodes.

    Args:
        variable: The right-most variable
        deriv  : Its derivative that we want to propagate backward to the leaves.

    No return. Should write to its results to the derivative values of each leaf through `accumulate_derivative`.
    """
    order = topological_sort(variable)
    derivatives = {variable.unique_id: deriv}

    for var in order:
        d_output = derivatives[var.unique_id]
        if var.is_leaf():
            var.accumulate_derivative(d_output)
        else:
            for parent, d_in in var.chain_rule(d_output):
                if parent.is_constant():
                    continue
                if parent.unique_id in derivatives:
                    derivatives[parent.unique_id] += d_in
                else:
                    derivatives[parent.unique_id] = d_in

@dataclass
class Context:
    """
    Context class is used by `Function` to store information during the forward pass.
    """

    no_grad: bool = False
    saved_values: Tuple[Any, ...] = ()

    def save_for_backward(self, *values: Any) -> None:
        "Store the given `values` if they need to be used during backpropagation."
        if self.no_grad:
            return
        self.saved_values = values

    @property
    def saved_tensors(self) -> Tuple[Any, ...]:
        return self.saved_values
