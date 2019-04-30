#
# PySNMP MIB module Papouch-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Papouch-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 20:34:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ObjectIdentity, ModuleIdentity, Counter32, IpAddress, enterprises, iso, Unsigned32, MibIdentifier, TimeTicks, Integer32, Bits, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter32", "IpAddress", "enterprises", "iso", "Unsigned32", "MibIdentifier", "TimeTicks", "Integer32", "Bits", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
papouchProjekt = ModuleIdentity((1, 3, 6, 1, 4, 1, 18248))
papouchProjekt.setRevisions(('2006-04-07 00:00',))
if mibBuilder.loadTexts: papouchProjekt.setLastUpdated('200604070000Z')
if mibBuilder.loadTexts: papouchProjekt.setOrganization('PaPouch s.r.o')
tme = ObjectIdentity((1, 3, 6, 1, 4, 1, 18248, 1))
if mibBuilder.loadTexts: tme.setStatus('current')
quido = ObjectIdentity((1, 3, 6, 1, 4, 1, 18248, 2))
if mibBuilder.loadTexts: quido.setStatus('current')
eccitace = ObjectIdentity((1, 3, 6, 1, 4, 1, 18248, 3))
if mibBuilder.loadTexts: eccitace.setStatus('current')
e_monitor = ObjectIdentity((1, 3, 6, 1, 4, 1, 18248, 4))
if mibBuilder.loadTexts: e_monitor.setStatus('current')
mibBuilder.exportSymbols("Papouch-SMI", papouchProjekt=papouchProjekt, PYSNMP_MODULE_ID=papouchProjekt, tme=tme, e_monitor=e_monitor, quido=quido, eccitace=eccitace)
