#
# PySNMP MIB module Juniper-Dos-Protection-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Dos-Protection-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, Gauge32, IpAddress, Bits, ObjectIdentity, ModuleIdentity, MibIdentifier, Counter64, iso, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "Gauge32", "IpAddress", "Bits", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Counter64", "iso", "TimeTicks", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniDosProtectionAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 76))
juniDosProtectionAgent.setRevisions(('2006-07-01 00:00', '2006-01-01 00:00',))
if mibBuilder.loadTexts: juniDosProtectionAgent.setLastUpdated('200511111830Z')
if mibBuilder.loadTexts: juniDosProtectionAgent.setOrganization('Juniper Networks, Inc.')
juniDosProtectionAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 76, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionAgentV1 = juniDosProtectionAgentV1.setProductRelease('Version 1 of the Dos Protection component of the JUNOSe SNMP agent.\n        This version of the Dos Protection component is supported in JUNOSe 7.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionAgentV1 = juniDosProtectionAgentV1.setStatus('obsolete')
juniDosProtectionAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 76, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionAgentV2 = juniDosProtectionAgentV2.setProductRelease('Version 2 of the Dos Protection component of the JUNOSe SNMP agent.\n        This version of the Dos Protection component is supported in JUNOSe x.y\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionAgentV2 = juniDosProtectionAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-Dos-Protection-CONF", PYSNMP_MODULE_ID=juniDosProtectionAgent, juniDosProtectionAgentV1=juniDosProtectionAgentV1, juniDosProtectionAgentV2=juniDosProtectionAgentV2, juniDosProtectionAgent=juniDosProtectionAgent)
