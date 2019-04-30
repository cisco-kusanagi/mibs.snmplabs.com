#
# PySNMP MIB module CISCO-LWAPP-DOT11-CLIENT-CALIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-DOT11-CLIENT-CALIB-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:48:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, MibIdentifier, Bits, TimeTicks, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, ObjectIdentity, Counter32, IpAddress, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Bits", "TimeTicks", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "ObjectIdentity", "Counter32", "IpAddress", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLwappDot11ClientCalibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 502))
ciscoLwappDot11ClientCalibCapability.setRevisions(('2006-05-16 00:00',))
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setLastUpdated('200605160000Z')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setOrganization('Cisco Systems, Inc.')
ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 502, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0 = ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0 = ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-DOT11-CLIENT-CALIB-CAPABILITY", ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0=ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0, PYSNMP_MODULE_ID=ciscoLwappDot11ClientCalibCapability, ciscoLwappDot11ClientCalibCapability=ciscoLwappDot11ClientCalibCapability)
