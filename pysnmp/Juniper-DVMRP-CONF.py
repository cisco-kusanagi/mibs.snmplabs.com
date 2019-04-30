#
# PySNMP MIB module Juniper-DVMRP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DVMRP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, TimeTicks, Counter64, Counter32, Unsigned32, MibIdentifier, IpAddress, Gauge32, Integer32, Bits, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Counter64", "Counter32", "Unsigned32", "MibIdentifier", "IpAddress", "Gauge32", "Integer32", "Bits", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniDvmrpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 12))
juniDvmrpAgent.setRevisions(('2003-01-16 21:01', '2001-11-30 20:24',))
if mibBuilder.loadTexts: juniDvmrpAgent.setLastUpdated('200301162101Z')
if mibBuilder.loadTexts: juniDvmrpAgent.setOrganization('Juniper Networks, Inc.')
juniDvmrpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 12, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpAgentV1 = juniDvmrpAgentV1.setProductRelease('Version 1 of the DVMRP component of the JUNOSe SNMP agent.  This\n        version of the DVMRP component was supported in JUNOSe 3.0 thru 4.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpAgentV1 = juniDvmrpAgentV1.setStatus('obsolete')
juniDvmrpAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 12, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpAgentV2 = juniDvmrpAgentV2.setProductRelease('Version 2 of the DVMRP component of the JUNOSe SNMP agent.  This\n        version of the DVMRP component is supported in JUNOSe 5.0 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDvmrpAgentV2 = juniDvmrpAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-DVMRP-CONF", juniDvmrpAgent=juniDvmrpAgent, PYSNMP_MODULE_ID=juniDvmrpAgent, juniDvmrpAgentV1=juniDvmrpAgentV1, juniDvmrpAgentV2=juniDvmrpAgentV2)
