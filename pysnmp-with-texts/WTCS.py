#
# PySNMP MIB module WTCS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WTCS
# Produced by pysmi-0.3.4 at Wed May  1 13:53:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Bits, ObjectIdentity, Gauge32, ModuleIdentity, enterprises, Counter64, TimeTicks, MibIdentifier, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Bits", "ObjectIdentity", "Gauge32", "ModuleIdentity", "enterprises", "Counter64", "TimeTicks", "MibIdentifier", "IpAddress", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wtcs = ModuleIdentity((1, 3, 6, 1, 4, 1, 9600))
wtcs.setRevisions(('2004-02-29 06:16', '2003-11-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wtcs.setRevisionsDescriptions(('Modified InstanceName to be UTF-8 format based.', 'The initial revision of this MIB module.',))
if mibBuilder.loadTexts: wtcs.setLastUpdated('200402290616Z')
if mibBuilder.loadTexts: wtcs.setOrganization('Informant Systems, Inc.')
if mibBuilder.loadTexts: wtcs.setContactInfo('Garth Williams 11135-23A Ave Edmonton, AB T6J4W5 Canada Tel: +1 780 434 4113 E-mail: garth.williams@wtcs.org')
if mibBuilder.loadTexts: wtcs.setDescription('The Structure of Management Information for WTCS.')
class InstanceName(TextualConvention, OctetString):
    description = 'The instance name for a specific performance counter in UTF-8 format.'
    status = 'current'
    displayHint = '64t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

informant = MibIdentifier((1, 3, 6, 1, 4, 1, 9600, 1))
mibBuilder.exportSymbols("WTCS", InstanceName=InstanceName, wtcs=wtcs, informant=informant, PYSNMP_MODULE_ID=wtcs)
