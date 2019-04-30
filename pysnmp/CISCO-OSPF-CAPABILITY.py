#
# PySNMP MIB module CISCO-OSPF-CAPABILITY (http://pysnmp.sf.net)
# Produced by pysmi-0.0.1 from CISCO-OSPF-CAPABILITY at Fri May  8 20:20:05 2015
# On host cray platform Linux version 2.6.37.6-smp by user tt
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( ciscoAgentCapability, ) = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
( AgentCapabilities, ) = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities")
( Integer32, MibIdentifier, TimeTicks, iso, Gauge32, ModuleIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "TimeTicks", "iso", "Gauge32", "ModuleIdentity", "Bits", "Counter32")
ciscoOspfCapability = ModuleIdentity(ciscoAgentCapability.getName() + (287,)).setRevisions(("2002-11-26 00:00",))
ciscoOspfCapabilityV12R025S = AgentCapabilities(ciscoOspfCapability.getName() + (1,))
mibBuilder.exportSymbols("CISCO-OSPF-CAPABILITY", ciscoOspfCapability=ciscoOspfCapability, ciscoOspfCapabilityV12R025S=ciscoOspfCapabilityV12R025S, PYSNMP_MODULE_ID=ciscoOspfCapability)
