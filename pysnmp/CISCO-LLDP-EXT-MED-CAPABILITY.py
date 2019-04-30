#
# PySNMP MIB module CISCO-LLDP-EXT-MED-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LLDP-EXT-MED-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:47:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Gauge32, iso, MibIdentifier, ModuleIdentity, NotificationType, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Bits, ObjectIdentity, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "MibIdentifier", "ModuleIdentity", "NotificationType", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Bits", "ObjectIdentity", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLldpExtMedCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 584))
ciscoLldpExtMedCapability.setRevisions(('2009-12-02 00:00',))
if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setLastUpdated('200912020000Z')
if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setOrganization('Cisco Systems, Inc.')
lldpExtMedCapability1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 584, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpExtMedCapability1 = lldpExtMedCapability1.setProductRelease('Cisco IOS 12.2SE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpExtMedCapability1 = lldpExtMedCapability1.setStatus('current')
mibBuilder.exportSymbols("CISCO-LLDP-EXT-MED-CAPABILITY", lldpExtMedCapability1=lldpExtMedCapability1, ciscoLldpExtMedCapability=ciscoLldpExtMedCapability, PYSNMP_MODULE_ID=ciscoLldpExtMedCapability)
