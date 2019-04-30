#
# PySNMP MIB module CISCO-MAC-AUTH-BYPASS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MAC-AUTH-BYPASS-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:49:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, Counter32, MibIdentifier, Counter64, Gauge32, Unsigned32, ModuleIdentity, Integer32, Bits, ObjectIdentity, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Counter32", "MibIdentifier", "Counter64", "Gauge32", "Unsigned32", "ModuleIdentity", "Integer32", "Bits", "ObjectIdentity", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMacAuthBypassCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 574))
ciscoMacAuthBypassCapability.setRevisions(('2010-03-09 00:00', '2008-10-30 00:00',))
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setLastUpdated('201003090000Z')
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setOrganization('Cisco Systems, Inc.')
ciscoMabCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 574, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0233SXIPCat6K = ciscoMabCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0233SXIPCat6K = ciscoMabCapV12R0233SXIPCat6K.setStatus('current')
ciscoMabCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 574, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0252SGPCat4K = ciscoMabCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0252SGPCat4K = ciscoMabCapV12R0252SGPCat4K.setStatus('current')
mibBuilder.exportSymbols("CISCO-MAC-AUTH-BYPASS-CAPABILITY", ciscoMabCapV12R0252SGPCat4K=ciscoMabCapV12R0252SGPCat4K, PYSNMP_MODULE_ID=ciscoMacAuthBypassCapability, ciscoMacAuthBypassCapability=ciscoMacAuthBypassCapability, ciscoMabCapV12R0233SXIPCat6K=ciscoMabCapV12R0233SXIPCat6K)
