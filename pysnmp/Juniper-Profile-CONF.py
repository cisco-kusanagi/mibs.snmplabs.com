#
# PySNMP MIB module Juniper-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Profile-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
juniProfileAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniProfileAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, IpAddress, ModuleIdentity, iso, Counter64, NotificationType, TimeTicks, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "IpAddress", "ModuleIdentity", "iso", "Counter64", "NotificationType", "TimeTicks", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniProfileManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1))
juniProfileManagerAgent.setRevisions(('2002-12-17 20:00', '2002-09-06 16:54', '2001-03-29 18:00',))
if mibBuilder.loadTexts: juniProfileManagerAgent.setLastUpdated('200212172000Z')
if mibBuilder.loadTexts: juniProfileManagerAgent.setOrganization('Juniper Networks, Inc.')
juniProfileManagerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniProfileManagerAgentV1 = juniProfileManagerAgentV1.setProductRelease('Version 1 of the Profile Manager component of the JUNOSe SNMP agent.\n        This version of the Profile Manager component was supported in JUNOSe\n        1.1 thru 1.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniProfileManagerAgentV1 = juniProfileManagerAgentV1.setStatus('obsolete')
juniProfileManagerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniProfileManagerAgentV2 = juniProfileManagerAgentV2.setProductRelease('Version 2 of the Profile Manager component of the JUNOSe SNMP agent.\n        This version of the Profile Manager component was supported in JUNOSe\n        2.0 thru 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniProfileManagerAgentV2 = juniProfileManagerAgentV2.setStatus('obsolete')
juniProfileManagerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniProfileManagerAgentV3 = juniProfileManagerAgentV3.setProductRelease('Version 3 of the Profile Manager component of the JUNOSe SNMP agent.\n        This version of the Profile Manager component is supported in JUNOSe 5.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniProfileManagerAgentV3 = juniProfileManagerAgentV3.setStatus('current')
mibBuilder.exportSymbols("Juniper-Profile-CONF", juniProfileManagerAgentV1=juniProfileManagerAgentV1, juniProfileManagerAgentV3=juniProfileManagerAgentV3, juniProfileManagerAgentV2=juniProfileManagerAgentV2, juniProfileManagerAgent=juniProfileManagerAgent, PYSNMP_MODULE_ID=juniProfileManagerAgent)
