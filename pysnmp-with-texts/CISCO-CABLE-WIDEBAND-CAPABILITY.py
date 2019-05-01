#
# PySNMP MIB module CISCO-CABLE-WIDEBAND-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CABLE-WIDEBAND-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:52:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter32, iso, Gauge32, ObjectIdentity, Counter64, IpAddress, TimeTicks, ModuleIdentity, Unsigned32, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Gauge32", "ObjectIdentity", "Counter64", "IpAddress", "TimeTicks", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType")
StorageType, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "TextualConvention", "DisplayString")
ciscoCableWidebandCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 520))
ciscoCableWidebandCapability.setRevisions(('2010-06-09 00:00', '2006-09-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCableWidebandCapability.setRevisionsDescriptions(('Add notInService status for ccwbRFChannelRowStatus', 'This is the Initial version',))
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setLastUpdated('201006090000Z')
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setContactInfo('Cisco Systems Customer Service Postal: Cisco Systems 170 West Tasman Drive San Jose, CA 95134 U.S.A. Phone: +1 800 553-NETS E-mail: cs-ubr@cisco.com')
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setDescription('Agent capabilities for CISCO-CABLE-WIDEBAND-MIB')
ciscoCableWidebandCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 520, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV12R00 = ciscoCableWidebandCapabilityV12R00.setProductRelease('Cisco IOS 12.3BC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV12R00 = ciscoCableWidebandCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCableWidebandCapabilityV12R00.setDescription('Cisco Cable Wideband MIB capabilities.')
ciscoCableWidebandCapabilityV122R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 520, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV122R00 = ciscoCableWidebandCapabilityV122R00.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV122R00 = ciscoCableWidebandCapabilityV122R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCableWidebandCapabilityV122R00.setDescription('Cisco Cable Wideband MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CABLE-WIDEBAND-CAPABILITY", ciscoCableWidebandCapability=ciscoCableWidebandCapability, PYSNMP_MODULE_ID=ciscoCableWidebandCapability, ciscoCableWidebandCapabilityV12R00=ciscoCableWidebandCapabilityV12R00, ciscoCableWidebandCapabilityV122R00=ciscoCableWidebandCapabilityV122R00)
