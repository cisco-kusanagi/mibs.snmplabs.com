#
# PySNMP MIB module CISCO-NTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NTP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Gauge32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, ModuleIdentity, iso, ObjectIdentity, Unsigned32, Integer32, Counter64, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "ModuleIdentity", "iso", "ObjectIdentity", "Unsigned32", "Integer32", "Counter64", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoNtpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 99999))
ciscoNtpCapability.setRevisions(('2006-04-05 00:00', '2005-06-22 00:00', '2003-04-08 00:00',))
if mibBuilder.loadTexts: ciscoNtpCapability.setLastUpdated('200604050000Z')
if mibBuilder.loadTexts: ciscoNtpCapability.setOrganization('Cisco Systems, Inc.')
ciscoNtpCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityV3R00 = ciscoNtpCapabilityV3R00.setProductRelease('MGX8850 Release 3.00,BPX SES Release ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityV3R00 = ciscoNtpCapabilityV3R00.setStatus('current')
ciscoNtpCapabilitySANOSV3R0001 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilitySANOSV3R0001 = ciscoNtpCapabilitySANOSV3R0001.setProductRelease('SAN-OS 3.0(1) ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilitySANOSV3R0001 = ciscoNtpCapabilitySANOSV3R0001.setStatus('current')
ciscoNtpCapabilityIOS124 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityIOS124 = ciscoNtpCapabilityIOS124.setProductRelease('IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityIOS124 = ciscoNtpCapabilityIOS124.setStatus('current')
mibBuilder.exportSymbols("CISCO-NTP-CAPABILITY", ciscoNtpCapabilitySANOSV3R0001=ciscoNtpCapabilitySANOSV3R0001, ciscoNtpCapability=ciscoNtpCapability, PYSNMP_MODULE_ID=ciscoNtpCapability, ciscoNtpCapabilityV3R00=ciscoNtpCapabilityV3R00, ciscoNtpCapabilityIOS124=ciscoNtpCapabilityIOS124)
