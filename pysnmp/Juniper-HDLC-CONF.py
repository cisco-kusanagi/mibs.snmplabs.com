#
# PySNMP MIB module Juniper-HDLC-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-HDLC-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
NotificationType, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, iso, Unsigned32, IpAddress, Bits, MibIdentifier, Counter32, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "iso", "Unsigned32", "IpAddress", "Bits", "MibIdentifier", "Counter32", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniHdlcAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18))
juniHdlcAgent.setRevisions(('2003-09-29 15:19', '2002-09-06 16:54', '2001-03-28 14:17',))
if mibBuilder.loadTexts: juniHdlcAgent.setLastUpdated('200309291519Z')
if mibBuilder.loadTexts: juniHdlcAgent.setOrganization('Juniper Networks, Inc.')
juniHdlcAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV1 = juniHdlcAgentV1.setProductRelease('Version 1 of the HDLC component of the JUNOSe SNMP agent.  This version\n        of the HDLC component was supported in JUNOSe 1.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV1 = juniHdlcAgentV1.setStatus('obsolete')
juniHdlcAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV2 = juniHdlcAgentV2.setProductRelease('Version 2 of the HDLC component of the JUNOSe SNMP agent.  This version\n        of the HDLC component was supported in JUNOSe 1.1 thru 3.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV2 = juniHdlcAgentV2.setStatus('obsolete')
juniHdlcAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV3 = juniHdlcAgentV3.setProductRelease('Version 3 of the HDLC component of the JUNOSe SNMP agent.  This version\n        of the HDLC component is supported in JUNOSe 3.1 through 5.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV3 = juniHdlcAgentV3.setStatus('obsolete')
juniHdlcAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV4 = juniHdlcAgentV4.setProductRelease('Version 3 of the HDLC component of the JUNOSe SNMP agent.  This version\n        of the HDLC component is supported in JUNOSe 5.1 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcAgentV4 = juniHdlcAgentV4.setStatus('current')
mibBuilder.exportSymbols("Juniper-HDLC-CONF", juniHdlcAgentV1=juniHdlcAgentV1, juniHdlcAgentV2=juniHdlcAgentV2, juniHdlcAgentV3=juniHdlcAgentV3, juniHdlcAgent=juniHdlcAgent, juniHdlcAgentV4=juniHdlcAgentV4, PYSNMP_MODULE_ID=juniHdlcAgent)
