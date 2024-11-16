<div align="center">
  <h1 align="center">awesome zkVm</h1>

A curated list of zkVM, zero-knowledge virtual machine.

  <p align="center">
    <a href="https://github.com/sindresorhus/awesome">
      <img alt="awesome list badge" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg">
    </a>
    <a href="https://github.com/rkdud007/awesome-zkvm/graphs/contributors">
      <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/rkdud007/awesome-zkvm">
    </a>
    <a href="http://makeapullrequest.com">
      <img alt="pull requests welcome badge" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat">
    </a>
  </p>

</div>

[Contributions](./CONTRIBUTING.md) and suggestions are always welcome; open issues or pull requests with any changes you want to be made.

# contents

- [projects repositories](#projects-repositories)
- [bench](#bench)
- [papers](#papers)
- [resources](#resources)
- [tutorials](#tutorials)
- [architecture](#architecture)
  - [precompiles](#precompiles)
  - [recursion](#recursion)
  - [lookup arguments](#lookup-arguments)
  - [hardware](#hardware)
- [related awesome lists](#related-awesome-lists)

## projects repositories

- [cairo](https://github.com/lambdaclass/cairo-vm)
- [eigen zkvm](https://github.com/0xEigenLabs/eigen-zkvm)
- [jolt](https://github.com/a16z/jolt)
- [miden](https://github.com/0xPolygonMiden/miden-vm)
- [nexus](https://github.com/nexus-xyz/nexus-zkvm)
- [o1vm](https://github.com/o1-labs/proof-systems/tree/master/o1vm)
- [olavm](https://github.com/Sin7Y/olavm)
- [powdr](https://github.com/powdr-labs/powdr)
- [risc0](https://github.com/risc0/risc0)
- [sp1](https://github.com/succinctlabs/sp1)
- [sphinx](https://github.com/argumentcomputer/sphinx)
- [triton vm](https://github.com/TritonVM/triton-vm)
- [valida](https://github.com/valida-xyz/valida)
- [zkWasm](https://github.com/DelphinusLab/zkWasm)

## bench

- [benchmarks (lita)](https://lita.gitbook.io/lita-documentation/architecture/benchmarks)
- [benchmark (risc0)](https://reports.risczero.com/benchmarks/Linux-cpu)
- [zkvm-benchmarks (a16z)](https://github.com/a16z/zkvm-benchmarks)
- [zkvm perf (succinct)](https://github.com/succinctlabs/zkvm-perf)

## papers

### Cairo

- [Cairo – a Turing-complete STARK-friendly CPU architecture](https://eprint.iacr.org/2021/1063.pdf)
- [A Verified Algebraic Representation of Cairo Program Execution](https://dl.acm.org/doi/pdf/10.1145/3497775.3503675)
- [A Proof-Producing Compiler for Blockchain Applications](https://drops.dagstuhl.de/storage/00lipics/lipics-vol268-itp2023/LIPIcs.ITP.2023.7/LIPIcs.ITP.2023.7.pdf)

### Jolt

- [Jolt: SNARKs for Virtual Machines via Lookups](https://eprint.iacr.org/2023/1217.pdf)

### Risc Zero

- [RISC Zero zkVM: Scalable, Transparent Arguments of RISC-V Integrity](https://dev.risczero.com/proof-system-in-detail.pdf)

## resources

- [a zero-knowledge paradigm series](https://www.lita.foundation/blog/zero-knowledge-paradigm-zkvm)
- [cairo – a turing-complete stark-friendly cpu architecture - shahar papini](https://www.youtube.com/watch?v=vVgHL5vpJxY&t=33s)
- [lasso + jolt playlist](https://youtube.com/playlist?list=PLjQ9HCQMu_8xjOEM_vh5p26ODtr-mmGxO&si=Uega8IMg_J8kNaa8)
- [new paradigm in ethereum l2 scaling: multi-proving and zk-vms](https://www.mikkoikola.com/blog/2023/12/11/new-paradigm-in-ethereum-l2-scaling-multi-proving-and-zk-vms)
- [the nexus v1.0 zkvm - daniel marin (nexus)](https://www.youtube.com/watch?v=UtzFOwQp8n4)
- [understanding jolt: clarifications and reflections](https://a16zcrypto.com/posts/article/understanding-jolt-clarifications-and-reflections/)
- [zk whiteboard sessions – module seven: zero knowledge virtual machines (zkvm) with grjte](https://www.youtube.com/watch?v=GRFPGJW0hic)
- [zk10: analysis of zkvm designs - wei dai & terry chung](https://www.youtube.com/watch?v=tWJZX-WmbeY&t=325s)
- [zk11: o1vm: building a real-world zkvm for mips - danny willems](https://www.youtube.com/watch?v=HDH2KXRAxAc)
- [zk12: memory checking in ivc-based zkvm - jens groth](https://www.youtube.com/watch?v=kzSYNFh4uQ0&list=PLothk45x3HC9Oz4f3e9-OoYUEytfHWCl5)
- [zk7: miden vm: a stark-friendly vm for blockchains - bobbin threadbare – polygon](https://www.youtube.com/watch?v=81UAaiIgIYA&t=803s)
- [zeroing into zkvm](https://taiko.mirror.xyz/e_5GeGGFJIrOxqvXOfzY6HmWcRjCjRyG0NQF1zbNpNQ)
- [zkvm design walkthrough with max and daniel](https://www.youtube.com/watch?v=aobrJ-zTcAU)
- [Verification of zkWasm in Coq](https://github.com/CertiKProject/zkwasm-fv)
- [zk11: polynomial acceleration for stark vms](https://www.youtube.com/watch?v=R07ina4k7hg)
- [what does risc v have to do with risc zero's zkvm](https://www.youtube.com/watch?v=11DIflEwx50)
- [risc zero architecture presentation @ stanford](https://www.youtube.com/watch?v=RtGk6967PC4)
- [continuations: scaling in zkvm](https://www.youtube.com/watch?v=h1qWnf-M5lo)

## tutorials

- [brainfuck tutorial](https://neptune.cash/learn/brainfuck-tutorial/)
- [fri from scratch](https://blog.lambdaclass.com/how-to-code-fri-from-scratch/)
- [stark by hand](https://dev.risczero.com/proof-system/stark-by-hand)
- [stark brainfuck](https://aszepieniec.github.io/stark-brainfuck/)
- [stark 101](https://starkware.co/stark-101/)

## related awesome lists

- [awesome risc0](https://github.com/inversebrah/awesome-risc0)
- [awesome sp1](https://github.com/gakonst/awesome-sp1)
- [awesome starknet #cryptography-and-maths](https://github.com/keep-starknet-strange/awesome-starknet?tab=readme-ov-file#cryptography-and-maths)
- [awesome zkp](https://github.com/matter-labs/awesome-zero-knowledge-proofs)
