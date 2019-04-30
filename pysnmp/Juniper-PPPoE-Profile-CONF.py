#
# PySNMP MIB module Juniper-PPPoE-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-PPPoE-Profile-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
juniProfileAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniProfileAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, Unsigned32, Gauge32, ObjectIdentity, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Counter64, ModuleIdentity, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Unsigned32", "Gauge32", "ObjectIdentity", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Counter64", "ModuleIdentity", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniPppoeProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4))
juniPppoeProfileAgent.setRevisions(('2005-07-13 11:40', '2004-06-14 20:48', '2003-03-13 18:01', '2002-09-06 16:54', '2002-08-15 20:38', '2002-05-31 18:21',))
if mibBuilder.loadTexts: juniPppoeProfileAgent.setLastUpdated('200507131140Z')
if mibBuilder.loadTexts: juniPppoeProfileAgent.setOrganization('Juniper Networks, Inc.')
juniPppoeProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV1 = juniPppoeProfileAgentV1.setProductRelease('Version 1 of the PPPoE Profile component of the JUNOSe SNMP agent.\n        This version of the PPPoE Profile component was supported in JUNOSe 3.0\n        and 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV1 = juniPppoeProfileAgentV1.setStatus('obsolete')
juniPppoeProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV2 = juniPppoeProfileAgentV2.setProductRelease('Version 2 of the PPPoE Profile component of the JUNOSe SNMP agent.\n        This version of the PPPoE Profile component was supported in JUNOSe 3.2\n        and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV2 = juniPppoeProfileAgentV2.setStatus('obsolete')
juniPppoeProfileAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV3 = juniPppoeProfileAgentV3.setProductRelease('Version 3 of the PPPoE Profile component of the JUNOSe SNMP agent.\n        This version of the PPPoE Profile component was supported in JUNOSe 4.0\n        thru 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV3 = juniPppoeProfileAgentV3.setStatus('obsolete')
juniPppoeProfileAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV4 = juniPppoeProfileAgentV4.setProductRelease('Version 4 of the PPPoE component of the JUNOSe SNMP agent.  This\n        version of the PPPoE component was supported in JUNOSe 5.1 through 7.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV4 = juniPppoeProfileAgentV4.setStatus('obsolete')
juniPppoeProfileAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV5 = juniPppoeProfileAgentV5.setProductRelease('Version 5 of the PPPoE Profile component of the JUNOSe SNMP agent.\n        This version of the PPPoE Profile component is supported in JUNOSe 7.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV5 = juniPppoeProfileAgentV5.setStatus('obsolete')
juniPppoeProfileAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV6 = juniPppoeProfileAgentV6.setProductRelease('Version 6 of the PPPoE Profile component of the JUNOSe SNMP agent.\n        This version of the PPPoE Profile component is supported in JUNOSe 7.0.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileAgentV6 = juniPppoeProfileAgentV6.setStatus('current')
mibBuilder.exportSymbols("Juniper-PPPoE-Profile-CONF", juniPppoeProfileAgentV3=juniPppoeProfileAgentV3, PYSNMP_MODULE_ID=juniPppoeProfileAgent, juniPppoeProfileAgent=juniPppoeProfileAgent, juniPppoeProfileAgentV5=juniPppoeProfileAgentV5, juniPppoeProfileAgentV2=juniPppoeProfileAgentV2, juniPppoeProfileAgentV1=juniPppoeProfileAgentV1, juniPppoeProfileAgentV6=juniPppoeProfileAgentV6, juniPppoeProfileAgentV4=juniPppoeProfileAgentV4)
