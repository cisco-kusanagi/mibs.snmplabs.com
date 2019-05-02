#
# PySNMP MIB module PACKETFRONT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PACKETFRONT-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:36:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
pfModules, = mibBuilder.importSymbols("PACKETFRONT-SMI", "pfModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Unsigned32, MibIdentifier, ObjectIdentity, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, NotificationType, Counter32, IpAddress, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "MibIdentifier", "ObjectIdentity", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "NotificationType", "Counter32", "IpAddress", "Bits", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pfTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9303, 5, 1))
pfTextualConventions.setRevisions(('2009-03-23 10:40', '2008-05-01 08:39', '2007-05-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pfTextualConventions.setRevisionsDescriptions(('Update telephone number in contact-info, reorder revision information', 'Added Unsigned64 object type', 'Added PortList object type',))
if mibBuilder.loadTexts: pfTextualConventions.setLastUpdated('200903231040Z')
if mibBuilder.loadTexts: pfTextualConventions.setOrganization('PacketFront Systems AB')
if mibBuilder.loadTexts: pfTextualConventions.setContactInfo('PacketFront Systems AB Customer Service Mail : Isafjordsgatan 35 SE-164 28 Kista Sweden Tel : +46 8 5090 1500 E-mail: snmp@packetfront.com Web : http://www.packetfront.com')
if mibBuilder.loadTexts: pfTextualConventions.setDescription('This module defines textual conventions used throughout Packetfront enterprise mibs.')
class PortList(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'."
    status = 'current'

mibBuilder.exportSymbols("PACKETFRONT-TC", PYSNMP_MODULE_ID=pfTextualConventions, PortList=PortList, pfTextualConventions=pfTextualConventions)
