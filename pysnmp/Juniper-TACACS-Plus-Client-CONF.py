#
# PySNMP MIB module Juniper-TACACS-Plus-Client-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-TACACS-Plus-Client-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
iso, TimeTicks, ModuleIdentity, ObjectIdentity, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Integer32, IpAddress, Unsigned32, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Integer32", "IpAddress", "Unsigned32", "MibIdentifier", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniTacacsPlusClientAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 57))
juniTacacsPlusClientAgent.setRevisions(('2004-03-02 17:31', '2002-09-06 16:54', '2002-04-08 14:37',))
if mibBuilder.loadTexts: juniTacacsPlusClientAgent.setLastUpdated('200403021731Z')
if mibBuilder.loadTexts: juniTacacsPlusClientAgent.setOrganization('Juniper Networks, Inc.')
juniTacacsPlusClientAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 57, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusClientAgentV1 = juniTacacsPlusClientAgentV1.setProductRelease('Version 1 of the TACACS+ Client component of the JUNOSe SNMP agent.\n        This version of the TACACS+ Client component is supported in JUNOSe 4.1\n        through JUNOSe 5.2.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusClientAgentV1 = juniTacacsPlusClientAgentV1.setStatus('obsolete')
juniTacacsPlusClientAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 57, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusClientAgentV2 = juniTacacsPlusClientAgentV2.setProductRelease('Version 2 of the Tacacs Plus Client component of the JUNOSe SNMP agent.\n        This version of the Tacacs Plus Client component is supported in JUNOSe\n        5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusClientAgentV2 = juniTacacsPlusClientAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-TACACS-Plus-Client-CONF", juniTacacsPlusClientAgent=juniTacacsPlusClientAgent, PYSNMP_MODULE_ID=juniTacacsPlusClientAgent, juniTacacsPlusClientAgentV1=juniTacacsPlusClientAgentV1, juniTacacsPlusClientAgentV2=juniTacacsPlusClientAgentV2)
