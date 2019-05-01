#
# PySNMP MIB module CISCO-OSPF-CAPABILITY (http://pysnmp.sf.net)
# Produced by pysmi-0.0.1 from CISCO-OSPF-CAPABILITY at Fri May  8 20:20:45 2015
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
if mibBuilder.loadTexts: ciscoOspfCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoOspfCapability.setContactInfo('        Cisco Systems\n                                Customer Service\n\n                        Postal:        170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n\n                           Tel:        +1 800 553-NETS\n\n                        E-mail:        cs-ospf@cisco.com')
if mibBuilder.loadTexts: ciscoOspfCapability.setDescription('Agent capabilities for the OSPF MIB.')
ciscoOspfCapabilityV12R025S = AgentCapabilities(ciscoOspfCapability.getName() + (1,))
if mibBuilder.loadTexts: ciscoOspfCapabilityV12R025S.setDescription('CISCO-OSPF-MIB capabilites')
mibBuilder.exportSymbols("CISCO-OSPF-CAPABILITY", ciscoOspfCapability=ciscoOspfCapability, ciscoOspfCapabilityV12R025S=ciscoOspfCapabilityV12R025S, PYSNMP_MODULE_ID=ciscoOspfCapability)
