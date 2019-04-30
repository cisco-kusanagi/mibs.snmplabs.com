#
# PySNMP MIB module CISCO-TCP-STD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TCP-STD-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Integer32, Gauge32, Unsigned32, iso, NotificationType, MibIdentifier, Counter32, IpAddress, Bits, ObjectIdentity, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Unsigned32", "iso", "NotificationType", "MibIdentifier", "Counter32", "IpAddress", "Bits", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTcpStdCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 481))
ciscoTcpStdCapability.setRevisions(('2008-08-11 00:00', '2008-02-08 00:00', '2006-11-08 00:00', '2006-10-25 00:00', '2006-05-26 00:00', '2006-02-06 00:00',))
if mibBuilder.loadTexts: ciscoTcpStdCapability.setLastUpdated('200808110000Z')
if mibBuilder.loadTexts: ciscoTcpStdCapability.setOrganization('Cisco Systems, Inc.')
ciscoTcpStdCapIOSXRV3R2CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R2CRS1 = ciscoTcpStdCapIOSXRV3R2CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R2CRS1 = ciscoTcpStdCapIOSXRV3R2CRS1.setStatus('current')
ciscoTcpStdCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapACSWV03R000 = ciscoTcpStdCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n\n                    for Application Control Engine(ACE)\n\n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapACSWV03R000 = ciscoTcpStdCapACSWV03R000.setStatus('current')
ciscoTcpStdCapCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTSV100 = ciscoTcpStdCapCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTSV100 = ciscoTcpStdCapCTSV100.setStatus('current')
ciscoTcpStdCapCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTMV1000 = ciscoTcpStdCapCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTMV1000 = ciscoTcpStdCapCTMV1000.setStatus('current')
ciscoTcpStdCapIOSXRV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R4CRS1 = ciscoTcpStdCapIOSXRV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R4CRS1 = ciscoTcpStdCapIOSXRV3R4CRS1.setStatus('current')
ciscoTcpStdCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapc4710aceVA1R700 = ciscoTcpStdCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapc4710aceVA1R700 = ciscoTcpStdCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-TCP-STD-CAPABILITY", ciscoTcpStdCapCTMV1000=ciscoTcpStdCapCTMV1000, ciscoTcpStdCapability=ciscoTcpStdCapability, ciscoTcpStdCapIOSXRV3R2CRS1=ciscoTcpStdCapIOSXRV3R2CRS1, ciscoTcpStdCapc4710aceVA1R700=ciscoTcpStdCapc4710aceVA1R700, ciscoTcpStdCapCTSV100=ciscoTcpStdCapCTSV100, ciscoTcpStdCapACSWV03R000=ciscoTcpStdCapACSWV03R000, PYSNMP_MODULE_ID=ciscoTcpStdCapability, ciscoTcpStdCapIOSXRV3R4CRS1=ciscoTcpStdCapIOSXRV3R4CRS1)
