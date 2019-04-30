#
# PySNMP MIB module PACKETFRONT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PACKETFRONT-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
pfModules, = mibBuilder.importSymbols("PACKETFRONT-SMI", "pfModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, ModuleIdentity, Integer32, Counter32, iso, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "ModuleIdentity", "Integer32", "Counter32", "iso", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pfTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9303, 5, 1))
pfTextualConventions.setRevisions(('2009-03-23 10:40', '2008-05-01 08:39', '2007-05-18 00:00',))
if mibBuilder.loadTexts: pfTextualConventions.setLastUpdated('200903231040Z')
if mibBuilder.loadTexts: pfTextualConventions.setOrganization('PacketFront Systems AB')
class PortList(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("PACKETFRONT-TC", PYSNMP_MODULE_ID=pfTextualConventions, pfTextualConventions=pfTextualConventions, PortList=PortList)
