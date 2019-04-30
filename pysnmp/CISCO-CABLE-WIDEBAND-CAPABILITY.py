#
# PySNMP MIB module CISCO-CABLE-WIDEBAND-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CABLE-WIDEBAND-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:34:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, ModuleIdentity, Unsigned32, IpAddress, Counter32, Counter64, NotificationType, Gauge32, ObjectIdentity, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "ModuleIdentity", "Unsigned32", "IpAddress", "Counter32", "Counter64", "NotificationType", "Gauge32", "ObjectIdentity", "Integer32", "MibIdentifier")
DisplayString, TextualConvention, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "StorageType")
ciscoCableWidebandCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 520))
ciscoCableWidebandCapability.setRevisions(('2010-06-09 00:00', '2006-09-07 00:00',))
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setLastUpdated('201006090000Z')
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setOrganization('Cisco Systems, Inc.')
ciscoCableWidebandCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 520, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV12R00 = ciscoCableWidebandCapabilityV12R00.setProductRelease('Cisco IOS 12.3BC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV12R00 = ciscoCableWidebandCapabilityV12R00.setStatus('current')
ciscoCableWidebandCapabilityV122R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 520, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV122R00 = ciscoCableWidebandCapabilityV122R00.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV122R00 = ciscoCableWidebandCapabilityV122R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-CABLE-WIDEBAND-CAPABILITY", ciscoCableWidebandCapability=ciscoCableWidebandCapability, PYSNMP_MODULE_ID=ciscoCableWidebandCapability, ciscoCableWidebandCapabilityV122R00=ciscoCableWidebandCapabilityV122R00, ciscoCableWidebandCapabilityV12R00=ciscoCableWidebandCapabilityV12R00)
