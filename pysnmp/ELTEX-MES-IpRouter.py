#
# PySNMP MIB module ELTEX-MES-IpRouter (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-IpRouter
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
eltMesOspf, = mibBuilder.importSymbols("ELTEX-MES-IP", "eltMesOspf")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Integer32, TimeTicks, ModuleIdentity, MibIdentifier, Counter64, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Integer32", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Counter64", "ObjectIdentity", "Gauge32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
eltOspfAuthTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 1), )
if mibBuilder.loadTexts: eltOspfAuthTable.setStatus('current')
eltOspfAuthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 1, 1), ).setIndexNames((0, "ELTEX-MES-IpRouter", "eltOspfIfIpAddress"), (0, "ELTEX-MES-IpRouter", "eltOspfAuthKeyId"))
if mibBuilder.loadTexts: eltOspfAuthEntry.setStatus('current')
eltOspfIfIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltOspfIfIpAddress.setStatus('current')
eltOspfAuthKeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltOspfAuthKeyId.setStatus('current')
eltOspfAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltOspfAuthKey.setStatus('current')
eltOspfAuthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltOspfAuthStatus.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-IpRouter", eltOspfIfIpAddress=eltOspfIfIpAddress, eltOspfAuthEntry=eltOspfAuthEntry, eltOspfAuthStatus=eltOspfAuthStatus, eltOspfAuthKeyId=eltOspfAuthKeyId, eltOspfAuthTable=eltOspfAuthTable, eltOspfAuthKey=eltOspfAuthKey)
