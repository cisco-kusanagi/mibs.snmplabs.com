#
# PySNMP MIB module Juniper-Dos-Protection-Platform-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Dos-Protection-Platform-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
ObjectIdentity, ModuleIdentity, Integer32, TimeTicks, Gauge32, Unsigned32, Bits, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Integer32", "TimeTicks", "Gauge32", "Unsigned32", "Bits", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniDosProtectionPlatformAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 77))
juniDosProtectionPlatformAgent.setRevisions(('2006-07-01 00:00', '2006-01-01 00:00',))
if mibBuilder.loadTexts: juniDosProtectionPlatformAgent.setLastUpdated('200511111831Z')
if mibBuilder.loadTexts: juniDosProtectionPlatformAgent.setOrganization('Juniper Networks, Inc.')
juniDosProtectionPlatformAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 77, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionPlatformAgentV1 = juniDosProtectionPlatformAgentV1.setProductRelease('Version 1 of the Dos Protection Platform component of the JUNOSe SNMP agent.\n        This version of the Dos Protection Platform component is supported in JUNOSe 7.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionPlatformAgentV1 = juniDosProtectionPlatformAgentV1.setStatus('current')
juniDosProtectionPlatformAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 77, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionPlatformAgentV2 = juniDosProtectionPlatformAgentV2.setProductRelease('Version 1 of the Dos Protection Platform component of the JUNOSe SNMP agent.\n        This version of the Dos Protection Platform component is supported in JUNOSe -.-\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionPlatformAgentV2 = juniDosProtectionPlatformAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-Dos-Protection-Platform-CONF", PYSNMP_MODULE_ID=juniDosProtectionPlatformAgent, juniDosProtectionPlatformAgent=juniDosProtectionPlatformAgent, juniDosProtectionPlatformAgentV2=juniDosProtectionPlatformAgentV2, juniDosProtectionPlatformAgentV1=juniDosProtectionPlatformAgentV1)
