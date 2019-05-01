#
# PySNMP MIB module CISCO-TCP-STD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TCP-STD-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:14:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter32, Gauge32, ModuleIdentity, Counter64, Unsigned32, TimeTicks, ObjectIdentity, Integer32, MibIdentifier, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "ModuleIdentity", "Counter64", "Unsigned32", "TimeTicks", "ObjectIdentity", "Integer32", "MibIdentifier", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoTcpStdCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 481))
ciscoTcpStdCapability.setRevisions(('2008-08-11 00:00', '2008-02-08 00:00', '2006-11-08 00:00', '2006-10-25 00:00', '2006-05-26 00:00', '2006-02-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTcpStdCapability.setRevisionsDescriptions(('Added newlines at the end of the MIB file.', 'Added ciscoTcpStdCapc4710aceVA1R700 agent capability for ACE 4710 Application Control Engine Appliance.', 'Added ciscoTcpStdCapIOSXRV3R4CRS1 agent capability for IOS XR 3.4', 'Added capability for Cisco TelePresence System (CTS) and Cisco TelePresence Manager (CTM) platforms.', 'Added capability statement ciscoTcpStdCapACSWV03R000', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTcpStdCapability.setLastUpdated('200808110000Z')
if mibBuilder.loadTexts: ciscoTcpStdCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTcpStdCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTcpStdCapability.setDescription('Agent capabilities for TCP-MIB')
ciscoTcpStdCapIOSXRV3R2CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R2CRS1 = ciscoTcpStdCapIOSXRV3R2CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R2CRS1 = ciscoTcpStdCapIOSXRV3R2CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpStdCapIOSXRV3R2CRS1.setDescription('TCP-MIB capabilities for IOS XR release 3.2.0')
ciscoTcpStdCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapACSWV03R000 = ciscoTcpStdCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n\n                    for Application Control Engine(ACE)\n\n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapACSWV03R000 = ciscoTcpStdCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpStdCapACSWV03R000.setDescription('TCP-MIB capabilities for ACSW 3.0')
ciscoTcpStdCapCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTSV100 = ciscoTcpStdCapCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTSV100 = ciscoTcpStdCapCTSV100.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpStdCapCTSV100.setDescription('TCP-MIB capabilities for CTS 1.0.0')
ciscoTcpStdCapCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTMV1000 = ciscoTcpStdCapCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTMV1000 = ciscoTcpStdCapCTMV1000.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpStdCapCTMV1000.setDescription('TCP-MIB capabilities for CTM 1.0.0.0')
ciscoTcpStdCapIOSXRV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R4CRS1 = ciscoTcpStdCapIOSXRV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R4CRS1 = ciscoTcpStdCapIOSXRV3R4CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpStdCapIOSXRV3R4CRS1.setDescription('TCP-MIB capabilities for IOS XR release 3.4')
ciscoTcpStdCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapc4710aceVA1R700 = ciscoTcpStdCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapc4710aceVA1R700 = ciscoTcpStdCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpStdCapc4710aceVA1R700.setDescription('TCP-MIB capabilities for ACSW A1(7)')
mibBuilder.exportSymbols("CISCO-TCP-STD-CAPABILITY", ciscoTcpStdCapCTMV1000=ciscoTcpStdCapCTMV1000, ciscoTcpStdCapIOSXRV3R2CRS1=ciscoTcpStdCapIOSXRV3R2CRS1, ciscoTcpStdCapACSWV03R000=ciscoTcpStdCapACSWV03R000, ciscoTcpStdCapCTSV100=ciscoTcpStdCapCTSV100, ciscoTcpStdCapc4710aceVA1R700=ciscoTcpStdCapc4710aceVA1R700, ciscoTcpStdCapability=ciscoTcpStdCapability, ciscoTcpStdCapIOSXRV3R4CRS1=ciscoTcpStdCapIOSXRV3R4CRS1, PYSNMP_MODULE_ID=ciscoTcpStdCapability)
