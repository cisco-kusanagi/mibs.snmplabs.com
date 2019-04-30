#
# PySNMP MIB module CISCO-DISMAN-EVENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DISMAN-EVENT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Integer32, iso, Unsigned32, Bits, Counter32, Counter64, NotificationType, IpAddress, ObjectIdentity, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Unsigned32", "Bits", "Counter32", "Counter64", "NotificationType", "IpAddress", "ObjectIdentity", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cdismanEventCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 473))
cdismanEventCapability.setRevisions(('2006-01-16 00:00',))
if mibBuilder.loadTexts: cdismanEventCapability.setLastUpdated('200601160000Z')
if mibBuilder.loadTexts: cdismanEventCapability.setOrganization('Cisco Systems, Inc.')
cdismanEventCapabilityIOSXRV3R2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 473, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdismanEventCapabilityIOSXRV3R2R0CRS1 = cdismanEventCapabilityIOSXRV3R2R0CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdismanEventCapabilityIOSXRV3R2R0CRS1 = cdismanEventCapabilityIOSXRV3R2R0CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-DISMAN-EVENT-CAPABILITY", cdismanEventCapability=cdismanEventCapability, PYSNMP_MODULE_ID=cdismanEventCapability, cdismanEventCapabilityIOSXRV3R2R0CRS1=cdismanEventCapabilityIOSXRV3R2R0CRS1)
