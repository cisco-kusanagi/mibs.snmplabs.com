#
# PySNMP MIB module CISCO-ATM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:50:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Bits, Counter64, Gauge32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, iso, MibIdentifier, Counter32, NotificationType, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Gauge32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "iso", "MibIdentifier", "Counter32", "NotificationType", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAtmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoAtmCapability.setRevisions(('2002-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmCapability.setRevisionsDescriptions(('Initial Version of the MIB module.',))
if mibBuilder.loadTexts: ciscoAtmCapability.setLastUpdated('200206120000Z')
if mibBuilder.loadTexts: ciscoAtmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoAtmCapability.setDescription('The Agent Capabilities for ATM-MIB.')
ciscoAtmCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmCapabilityV2R00 = ciscoAtmCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                BPX SES Release 1.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmCapabilityV2R00 = ciscoAtmCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmCapabilityV2R00.setDescription('ATM MIB Capabilities')
mibBuilder.exportSymbols("CISCO-ATM-CAPABILITY", PYSNMP_MODULE_ID=ciscoAtmCapability, ciscoAtmCapability=ciscoAtmCapability, ciscoAtmCapabilityV2R00=ciscoAtmCapabilityV2R00)
