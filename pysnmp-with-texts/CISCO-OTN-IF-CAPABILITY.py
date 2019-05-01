#
# PySNMP MIB module CISCO-OTN-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OTN-IF-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, Counter32, MibIdentifier, ObjectIdentity, Bits, Counter64, IpAddress, Unsigned32, Gauge32, ModuleIdentity, TimeTicks, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "MibIdentifier", "ObjectIdentity", "Bits", "Counter64", "IpAddress", "Unsigned32", "Gauge32", "ModuleIdentity", "TimeTicks", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoOtnIfMIBCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 562))
ciscoOtnIfMIBCapability.setRevisions(('2007-10-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoOtnIfMIBCapability.setRevisionsDescriptions(('First version of this MIB module.',))
if mibBuilder.loadTexts: ciscoOtnIfMIBCapability.setLastUpdated('200710200000Z')
if mibBuilder.loadTexts: ciscoOtnIfMIBCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoOtnIfMIBCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dwdm-mibs@cisco.com')
if mibBuilder.loadTexts: ciscoOtnIfMIBCapability.setDescription('capabilities description for CISCO-OTN-IF-MIB')
ciscoOtnIfCapIOSXRV3R06CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 562, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOtnIfCapIOSXRV3R06CRS1 = ciscoOtnIfCapIOSXRV3R06CRS1.setProductRelease('Cisco IOS-XR Release 3.6 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOtnIfCapIOSXRV3R06CRS1 = ciscoOtnIfCapIOSXRV3R06CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoOtnIfCapIOSXRV3R06CRS1.setDescription('Cisco OTN IF MIB capabilities for IOX-XR Release 3.6 for CRS 1')
mibBuilder.exportSymbols("CISCO-OTN-IF-CAPABILITY", PYSNMP_MODULE_ID=ciscoOtnIfMIBCapability, ciscoOtnIfMIBCapability=ciscoOtnIfMIBCapability, ciscoOtnIfCapIOSXRV3R06CRS1=ciscoOtnIfCapIOSXRV3R06CRS1)
