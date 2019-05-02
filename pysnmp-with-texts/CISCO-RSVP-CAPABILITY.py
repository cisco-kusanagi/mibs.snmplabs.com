#
# PySNMP MIB module CISCO-RSVP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RSVP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:11:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, Unsigned32, IpAddress, Integer32, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Counter32, Bits, MibIdentifier, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "IpAddress", "Integer32", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Counter32", "Bits", "MibIdentifier", "Counter64", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRsvpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 10000))
if mibBuilder.loadTexts: ciscoRsvpCapability.setLastUpdated('200206210000Z')
if mibBuilder.loadTexts: ciscoRsvpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRsvpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-rsvp@cisco.com')
if mibBuilder.loadTexts: ciscoRsvpCapability.setDescription('The Agent Capabilities for RSVP-MIB.')
ciscoRsvpCapabilityVismV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10000, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRsvpCapabilityVismV3R00 = ciscoRsvpCapabilityVismV3R00.setProductRelease('VISM Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRsvpCapabilityVismV3R00 = ciscoRsvpCapabilityVismV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoRsvpCapabilityVismV3R00.setDescription('RSVP MIB Capabilities.')
mibBuilder.exportSymbols("CISCO-RSVP-CAPABILITY", PYSNMP_MODULE_ID=ciscoRsvpCapability, ciscoRsvpCapabilityVismV3R00=ciscoRsvpCapabilityVismV3R00, ciscoRsvpCapability=ciscoRsvpCapability)
