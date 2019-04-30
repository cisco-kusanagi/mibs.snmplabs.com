#
# PySNMP MIB module Juniper-License-Mgr-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-License-Mgr-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
TimeTicks, ModuleIdentity, ObjectIdentity, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Counter64, Gauge32, NotificationType, Counter32, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Counter64", "Gauge32", "NotificationType", "Counter32", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniLicenseMgrAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 71))
juniLicenseMgrAgent.setRevisions(('2004-09-14 21:07',))
if mibBuilder.loadTexts: juniLicenseMgrAgent.setLastUpdated('200409142107Z')
if mibBuilder.loadTexts: juniLicenseMgrAgent.setOrganization('Juniper Networks, Inc.')
juniLicenseMgrAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 71, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLicenseMgrAgentV1 = juniLicenseMgrAgentV1.setProductRelease('Version 1 of the License Mgr component of the JUNOSe SNMP agent.\n        This version of the License Mgr component is supported in JUNOSe 6.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLicenseMgrAgentV1 = juniLicenseMgrAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-License-Mgr-CONF", juniLicenseMgrAgentV1=juniLicenseMgrAgentV1, PYSNMP_MODULE_ID=juniLicenseMgrAgent, juniLicenseMgrAgent=juniLicenseMgrAgent)
