#
# PySNMP MIB module Papouch-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Papouch-SMI
# Produced by pysmi-0.3.4 at Wed May  1 14:43:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, IpAddress, ObjectIdentity, Counter32, iso, enterprises, ModuleIdentity, Counter64, TimeTicks, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "IpAddress", "ObjectIdentity", "Counter32", "iso", "enterprises", "ModuleIdentity", "Counter64", "TimeTicks", "MibIdentifier", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
papouchProjekt = ModuleIdentity((1, 3, 6, 1, 4, 1, 18248))
papouchProjekt.setRevisions(('2006-04-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: papouchProjekt.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: papouchProjekt.setLastUpdated('200604070000Z')
if mibBuilder.loadTexts: papouchProjekt.setOrganization('PaPouch s.r.o')
if mibBuilder.loadTexts: papouchProjekt.setContactInfo(' PaPouch s.r.o Software development E-mail: steiger@papouch.com')
if mibBuilder.loadTexts: papouchProjekt.setDescription('The Structure of Management Information for the PaPouch elektronika enterprise')
tme = ObjectIdentity((1, 3, 6, 1, 4, 1, 18248, 1))
if mibBuilder.loadTexts: tme.setStatus('current')
if mibBuilder.loadTexts: tme.setDescription('.')
quido = ObjectIdentity((1, 3, 6, 1, 4, 1, 18248, 2))
if mibBuilder.loadTexts: quido.setStatus('current')
if mibBuilder.loadTexts: quido.setDescription('.')
eccitace = ObjectIdentity((1, 3, 6, 1, 4, 1, 18248, 3))
if mibBuilder.loadTexts: eccitace.setStatus('current')
if mibBuilder.loadTexts: eccitace.setDescription('.')
e_monitor = ObjectIdentity((1, 3, 6, 1, 4, 1, 18248, 4))
if mibBuilder.loadTexts: e_monitor.setStatus('current')
if mibBuilder.loadTexts: e_monitor.setDescription('.')
mibBuilder.exportSymbols("Papouch-SMI", quido=quido, tme=tme, eccitace=eccitace, e_monitor=e_monitor, papouchProjekt=papouchProjekt, PYSNMP_MODULE_ID=papouchProjekt)
