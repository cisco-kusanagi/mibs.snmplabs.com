#
# PySNMP MIB module TUBS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-SMI
# Produced by pysmi-0.3.4 at Wed May  1 15:27:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, Counter64, enterprises, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, MibIdentifier, Bits, Integer32, ModuleIdentity, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Counter64", "enterprises", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "MibIdentifier", "Bits", "Integer32", "ModuleIdentity", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tubs = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575))
tubs.setRevisions(('2002-07-01 15:00', '2002-05-16 15:00', '2000-02-09 00:00', '1997-02-14 10:23',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tubs.setRevisionsDescriptions(("Added ibrpibtomib for automatic PIB to MIB conversion via 'smidump -f smiv2'.", 'Added ibrpib for all PIBs that are temporarily assigned to the ibr tree until they get official assignments from IANA. Fixed CONTACT-INFO to contain the current address.', 'Changed the module name from TUBS-REGISTRATION to TUBS-SMI.', 'The initial revision.',))
if mibBuilder.loadTexts: tubs.setLastUpdated('200002090000Z')
if mibBuilder.loadTexts: tubs.setOrganization('TU Braunschweig')
if mibBuilder.loadTexts: tubs.setContactInfo('Juergen Schoenwaelder TU Braunschweig Muehlenpfordtstrasse 23, 1. OG 38106 Braunschweig Germany Tel: +49 531 391 3283 Fax: +49 531 391 5936 E-mail: schoenw@ibr.cs.tu-bs.de')
if mibBuilder.loadTexts: tubs.setDescription('The toplevel OID registration for the Technical University of Braunschweig, Germany.')
ibr = ObjectIdentity((1, 3, 6, 1, 4, 1, 1575, 1))
if mibBuilder.loadTexts: ibr.setStatus('current')
if mibBuilder.loadTexts: ibr.setDescription('The subtree delegated to the Department of Operating Systems and Computer Networks (Institut fuer Betriebssysteme und Rechnerverbund).')
ibrpib = ObjectIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 10))
if mibBuilder.loadTexts: ibrpib.setStatus('current')
if mibBuilder.loadTexts: ibrpib.setDescription('Only for PIBs that are temporarily assigned to the ibr tree until they get official assignments from IANA.')
ibrpibtomib = ObjectIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 11))
if mibBuilder.loadTexts: ibrpibtomib.setStatus('current')
if mibBuilder.loadTexts: ibrpibtomib.setDescription("Only for PIBs that are automatically converted to MIBs via 'smidump -f smiv2'.")
ibrmibtopib = ObjectIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 12))
if mibBuilder.loadTexts: ibrmibtopib.setStatus('current')
if mibBuilder.loadTexts: ibrmibtopib.setDescription("Only for MIBs that are automatically converted to PIBs via 'smidump -f sppi'.")
class IBRUnsigned64(TextualConvention, OctetString):
    description = 'A dummy type for automatic PIB to MIB conversion.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class IBRInteger64(TextualConvention, OctetString):
    description = 'A dummy type for automatic PIB to MIB conversion.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

mibBuilder.exportSymbols("TUBS-SMI", ibrpib=ibrpib, IBRInteger64=IBRInteger64, ibrpibtomib=ibrpibtomib, PYSNMP_MODULE_ID=tubs, IBRUnsigned64=IBRUnsigned64, ibr=ibr, tubs=tubs, ibrmibtopib=ibrmibtopib)
