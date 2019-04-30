#
# PySNMP MIB module CISCO-RSVP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RSVP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, ObjectIdentity, Unsigned32, TimeTicks, Counter32, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Bits, Integer32, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Unsigned32", "TimeTicks", "Counter32", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Bits", "Integer32", "Counter64", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRsvpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 10000))
if mibBuilder.loadTexts: ciscoRsvpCapability.setLastUpdated('200206210000Z')
if mibBuilder.loadTexts: ciscoRsvpCapability.setOrganization('Cisco Systems, Inc.')
ciscoRsvpCapabilityVismV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10000, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRsvpCapabilityVismV3R00 = ciscoRsvpCapabilityVismV3R00.setProductRelease('VISM Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRsvpCapabilityVismV3R00 = ciscoRsvpCapabilityVismV3R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-RSVP-CAPABILITY", ciscoRsvpCapabilityVismV3R00=ciscoRsvpCapabilityVismV3R00, ciscoRsvpCapability=ciscoRsvpCapability, PYSNMP_MODULE_ID=ciscoRsvpCapability)
