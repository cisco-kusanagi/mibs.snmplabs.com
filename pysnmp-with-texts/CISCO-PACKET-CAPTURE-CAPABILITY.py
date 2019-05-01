#
# PySNMP MIB module CISCO-PACKET-CAPTURE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PACKET-CAPTURE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, Gauge32, Counter64, IpAddress, ModuleIdentity, Unsigned32, iso, NotificationType, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Gauge32", "Counter64", "IpAddress", "ModuleIdentity", "Unsigned32", "iso", "NotificationType", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPacketCaptureCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 527))
ciscoPacketCaptureCapability.setRevisions(('2008-10-23 00:00', '2007-01-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setRevisionsDescriptions(('Added capability statement cpcCapV12R0233SXIPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setLastUpdated('200810230000Z')
if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setDescription('The capabilities description of CISCO-PACKET-CAPTURE-MIB.')
ciscoPacketCaptureCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 527, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPacketCaptureCatOSV08R0601 = ciscoPacketCaptureCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1) on devices with\n                    Supervisor 720 or Supervisor 32 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPacketCaptureCatOSV08R0601 = ciscoPacketCaptureCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: ciscoPacketCaptureCatOSV08R0601.setDescription('CISCO-PACKET-CAPTURE-MIB capabilities.')
cpcCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 527, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpcCapV12R0233SXIPCat6K = cpcCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpcCapV12R0233SXIPCat6K = cpcCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: cpcCapV12R0233SXIPCat6K.setDescription('CISCO-PACKET-CAPTURE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PACKET-CAPTURE-CAPABILITY", ciscoPacketCaptureCapability=ciscoPacketCaptureCapability, cpcCapV12R0233SXIPCat6K=cpcCapV12R0233SXIPCat6K, PYSNMP_MODULE_ID=ciscoPacketCaptureCapability, ciscoPacketCaptureCatOSV08R0601=ciscoPacketCaptureCatOSV08R0601)
