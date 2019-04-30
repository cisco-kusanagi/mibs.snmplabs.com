#
# PySNMP MIB module CISCO-PACKET-CAPTURE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PACKET-CAPTURE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibIdentifier, ObjectIdentity, Unsigned32, ModuleIdentity, NotificationType, TimeTicks, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Counter32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "NotificationType", "TimeTicks", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Counter32", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPacketCaptureCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 527))
ciscoPacketCaptureCapability.setRevisions(('2008-10-23 00:00', '2007-01-05 00:00',))
if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setLastUpdated('200810230000Z')
if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setOrganization('Cisco Systems, Inc.')
ciscoPacketCaptureCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 527, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPacketCaptureCatOSV08R0601 = ciscoPacketCaptureCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1) on devices with\n                    Supervisor 720 or Supervisor 32 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPacketCaptureCatOSV08R0601 = ciscoPacketCaptureCatOSV08R0601.setStatus('current')
cpcCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 527, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpcCapV12R0233SXIPCat6K = cpcCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpcCapV12R0233SXIPCat6K = cpcCapV12R0233SXIPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-PACKET-CAPTURE-CAPABILITY", cpcCapV12R0233SXIPCat6K=cpcCapV12R0233SXIPCat6K, PYSNMP_MODULE_ID=ciscoPacketCaptureCapability, ciscoPacketCaptureCapability=ciscoPacketCaptureCapability, ciscoPacketCaptureCatOSV08R0601=ciscoPacketCaptureCatOSV08R0601)
