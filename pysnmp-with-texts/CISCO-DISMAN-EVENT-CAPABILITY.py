#
# PySNMP MIB module CISCO-DISMAN-EVENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DISMAN-EVENT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:54:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Integer32, Gauge32, ObjectIdentity, NotificationType, MibIdentifier, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, ModuleIdentity, IpAddress, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "ObjectIdentity", "NotificationType", "MibIdentifier", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "ModuleIdentity", "IpAddress", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cdismanEventCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 473))
cdismanEventCapability.setRevisions(('2006-01-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cdismanEventCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cdismanEventCapability.setLastUpdated('200601160000Z')
if mibBuilder.loadTexts: cdismanEventCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cdismanEventCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com cs-snmp@cisco.com')
if mibBuilder.loadTexts: cdismanEventCapability.setDescription('The capabilities description of DISMAN-EVENT-MIB.')
cdismanEventCapabilityIOSXRV3R2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 473, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdismanEventCapabilityIOSXRV3R2R0CRS1 = cdismanEventCapabilityIOSXRV3R2R0CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdismanEventCapabilityIOSXRV3R2R0CRS1 = cdismanEventCapabilityIOSXRV3R2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: cdismanEventCapabilityIOSXRV3R2R0CRS1.setDescription('DISMAN-EVENT-MIB capabilities for IOS XR release 3.2.0')
mibBuilder.exportSymbols("CISCO-DISMAN-EVENT-CAPABILITY", cdismanEventCapabilityIOSXRV3R2R0CRS1=cdismanEventCapabilityIOSXRV3R2R0CRS1, PYSNMP_MODULE_ID=cdismanEventCapability, cdismanEventCapability=cdismanEventCapability)
