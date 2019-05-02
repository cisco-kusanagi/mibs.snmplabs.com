#
# PySNMP MIB module CISCO-MAC-AUTH-BYPASS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MAC-AUTH-BYPASS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:06:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, TimeTicks, Counter64, IpAddress, Integer32, Bits, Counter32, ModuleIdentity, Unsigned32, ObjectIdentity, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "TimeTicks", "Counter64", "IpAddress", "Integer32", "Bits", "Counter32", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMacAuthBypassCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 574))
ciscoMacAuthBypassCapability.setRevisions(('2010-03-09 00:00', '2008-10-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setRevisionsDescriptions(('Added capability statement ciscoMabCapV12R0252SGPCat4K. Added more VARIATION for ciscoMabCapV12R0233SXIPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setLastUpdated('201003090000Z')
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ibns@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setDescription('The capabilities description of CISCO-MAC-AUTH-BYPASS-MIB.')
ciscoMabCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 574, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0233SXIPCat6K = ciscoMabCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0233SXIPCat6K = ciscoMabCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoMabCapV12R0233SXIPCat6K.setDescription('CISCO-MAC-AUTH-BYPASS-MIB capabilities.')
ciscoMabCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 574, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0252SGPCat4K = ciscoMabCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0252SGPCat4K = ciscoMabCapV12R0252SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: ciscoMabCapV12R0252SGPCat4K.setDescription('CISCO-MAC-AUTH-BYPASS-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MAC-AUTH-BYPASS-CAPABILITY", ciscoMabCapV12R0252SGPCat4K=ciscoMabCapV12R0252SGPCat4K, ciscoMabCapV12R0233SXIPCat6K=ciscoMabCapV12R0233SXIPCat6K, ciscoMacAuthBypassCapability=ciscoMacAuthBypassCapability, PYSNMP_MODULE_ID=ciscoMacAuthBypassCapability)
