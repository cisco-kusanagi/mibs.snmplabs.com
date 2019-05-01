#
# PySNMP MIB module CISCO-INT-SERV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-INT-SERV-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Bits, iso, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Integer32, TimeTicks, ObjectIdentity, Counter32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "iso", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Integer32", "TimeTicks", "ObjectIdentity", "Counter32", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIntServCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
if mibBuilder.loadTexts: ciscoIntServCapability.setLastUpdated('200206210000Z')
if mibBuilder.loadTexts: ciscoIntServCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIntServCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-rsvp@cisco.com')
if mibBuilder.loadTexts: ciscoIntServCapability.setDescription('The Agent Capabilities for INT-SERV-MIB.')
ciscoIntServCapabilityVismV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIntServCapabilityVismV3R00 = ciscoIntServCapabilityVismV3R00.setProductRelease('VISM Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIntServCapabilityVismV3R00 = ciscoIntServCapabilityVismV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIntServCapabilityVismV3R00.setDescription('INT-SERV-MIB Capabilities.')
mibBuilder.exportSymbols("CISCO-INT-SERV-CAPABILITY", ciscoIntServCapabilityVismV3R00=ciscoIntServCapabilityVismV3R00, ciscoIntServCapability=ciscoIntServCapability, PYSNMP_MODULE_ID=ciscoIntServCapability)
