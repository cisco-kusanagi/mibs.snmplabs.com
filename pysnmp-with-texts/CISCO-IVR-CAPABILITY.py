#
# PySNMP MIB module CISCO-IVR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IVR-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, Counter32, iso, TimeTicks, MibIdentifier, Counter64, ObjectIdentity, Bits, Integer32, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Counter32", "iso", "TimeTicks", "MibIdentifier", "Counter64", "ObjectIdentity", "Bits", "Integer32", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIvrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 491))
ciscoIvrCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIvrCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoIvrCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoIvrCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIvrCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIvrCapability.setDescription('Agent capabilities for CISCO-IVR-MIB')
ciscoIvrCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 491, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIvrCapSanOSV30R1MDS9000 = ciscoIvrCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIvrCapSanOSV30R1MDS9000 = ciscoIvrCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoIvrCapSanOSV30R1MDS9000.setDescription('Cisco Inter Virutal Storage Area Network (Inter-VSAN) Routing MIB capabilities')
mibBuilder.exportSymbols("CISCO-IVR-CAPABILITY", PYSNMP_MODULE_ID=ciscoIvrCapability, ciscoIvrCapability=ciscoIvrCapability, ciscoIvrCapSanOSV30R1MDS9000=ciscoIvrCapSanOSV30R1MDS9000)
