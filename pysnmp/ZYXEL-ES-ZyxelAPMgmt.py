#
# PySNMP MIB module ZYXEL-ES-ZyxelAPMgmt (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-ES-ZyxelAPMgmt
# Produced by pysmi-0.3.4 at Mon Apr 29 21:43:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Unsigned32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Bits, Counter64, NotificationType, Counter32, TimeTicks, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Bits", "Counter64", "NotificationType", "Counter32", "TimeTicks", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelAPMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 4))
if mibBuilder.loadTexts: zyxelAPMgmt.setLastUpdated('201403100000Z')
if mibBuilder.loadTexts: zyxelAPMgmt.setOrganization('Enterprise Solution Zyxel')
operationMode = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("standalone", 1), ("controller", 2), ("managed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: operationMode.setStatus('current')
wlanAPTx = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 4, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlanAPTx.setStatus('current')
wlanAPRx = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 4, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlanAPRx.setStatus('current')
wlanAPDescription = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 4, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlanAPDescription.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-ES-ZyxelAPMgmt", PYSNMP_MODULE_ID=zyxelAPMgmt, operationMode=operationMode, wlanAPRx=wlanAPRx, wlanAPTx=wlanAPTx, zyxelAPMgmt=zyxelAPMgmt, wlanAPDescription=wlanAPDescription)
