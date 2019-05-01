#
# PySNMP MIB module TUBS-REGISTRATION (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-REGISTRATION
# Produced by pysmi-0.3.4 at Wed May  1 15:27:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, IpAddress, ModuleIdentity, enterprises, Counter64, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Counter32, Unsigned32, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "IpAddress", "ModuleIdentity", "enterprises", "Counter64", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Counter32", "Unsigned32", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tubs = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575))
tubs.setRevisions(('1997-02-14 10:23',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tubs.setRevisionsDescriptions(('The initial revision.',))
if mibBuilder.loadTexts: tubs.setLastUpdated('9702141023Z')
if mibBuilder.loadTexts: tubs.setOrganization('TU Braunschweig')
if mibBuilder.loadTexts: tubs.setContactInfo('Juergen Schoenwaelder TU Braunschweig Bueltenweg 74/75 38108 Braunschweig Germany Tel: +49 531 391 3249 Fax: +49 531 391 5936 E-mail: schoenw@ibr.cs.tu-bs.de')
if mibBuilder.loadTexts: tubs.setDescription('The toplevel OID registration for the Technical University of Braunschweig, Germany.')
ibr = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1))
mibBuilder.exportSymbols("TUBS-REGISTRATION", PYSNMP_MODULE_ID=tubs, tubs=tubs, ibr=ibr)
