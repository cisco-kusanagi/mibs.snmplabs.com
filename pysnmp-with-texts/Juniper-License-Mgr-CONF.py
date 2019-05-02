#
# PySNMP MIB module Juniper-License-Mgr-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-License-Mgr-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Counter64, MibIdentifier, Counter32, Gauge32, iso, ObjectIdentity, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Counter64", "MibIdentifier", "Counter32", "Gauge32", "iso", "ObjectIdentity", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniLicenseMgrAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 71))
juniLicenseMgrAgent.setRevisions(('2004-09-14 21:07',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniLicenseMgrAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: juniLicenseMgrAgent.setLastUpdated('200409142107Z')
if mibBuilder.loadTexts: juniLicenseMgrAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniLicenseMgrAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniLicenseMgrAgent.setDescription('The agent capabilities definitions for the License Mgr component of the SNMP agent in the Juniper E-series family of products.')
juniLicenseMgrAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 71, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLicenseMgrAgentV1 = juniLicenseMgrAgentV1.setProductRelease('Version 1 of the License Mgr component of the JUNOSe SNMP agent.\n        This version of the License Mgr component is supported in JUNOSe 6.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLicenseMgrAgentV1 = juniLicenseMgrAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniLicenseMgrAgentV1.setDescription('The MIB supported by the JUNOSe SNMP agent for the License Mgr application.')
mibBuilder.exportSymbols("Juniper-License-Mgr-CONF", juniLicenseMgrAgentV1=juniLicenseMgrAgentV1, juniLicenseMgrAgent=juniLicenseMgrAgent, PYSNMP_MODULE_ID=juniLicenseMgrAgent)
