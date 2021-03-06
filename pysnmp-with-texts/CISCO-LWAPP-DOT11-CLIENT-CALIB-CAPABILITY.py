#
# PySNMP MIB module CISCO-LWAPP-DOT11-CLIENT-CALIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-DOT11-CLIENT-CALIB-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:05:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
iso, Counter64, TimeTicks, MibIdentifier, Unsigned32, ModuleIdentity, Integer32, Gauge32, NotificationType, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "TimeTicks", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Integer32", "Gauge32", "NotificationType", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLwappDot11ClientCalibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 502))
ciscoLwappDot11ClientCalibCapability.setRevisions(('2006-05-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setRevisionsDescriptions(('Initial version of this MIB module. ',))
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setLastUpdated('200605160000Z')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setDescription('Agent capabilities for CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB. ')
ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 502, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0 = ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0 = ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0.setDescription('CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB capabilities. ')
mibBuilder.exportSymbols("CISCO-LWAPP-DOT11-CLIENT-CALIB-CAPABILITY", ciscoLwappDot11ClientCalibCapability=ciscoLwappDot11ClientCalibCapability, PYSNMP_MODULE_ID=ciscoLwappDot11ClientCalibCapability, ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0=ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0)
