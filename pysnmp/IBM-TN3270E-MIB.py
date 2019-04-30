#
# PySNMP MIB module IBM-TN3270E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBM-TN3270E-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:39:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, enterprises, MibIdentifier, Bits, IpAddress, TimeTicks, Unsigned32, Gauge32, iso, Counter32, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "enterprises", "MibIdentifier", "Bits", "IpAddress", "TimeTicks", "Unsigned32", "Gauge32", "iso", "Counter32", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibmtn3270eMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1))
ibmtn3270eConnRejectTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1), )
if mibBuilder.loadTexts: ibmtn3270eConnRejectTable.setStatus('mandatory')
ibmtn3270eConnRejectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1, 1), ).setIndexNames((0, "IBM-TN3270E-MIB", "ibmtn3270eConnRejectIndex"))
if mibBuilder.loadTexts: ibmtn3270eConnRejectEntry.setStatus('mandatory')
ibmtn3270eConnRejectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: ibmtn3270eConnRejectIndex.setStatus('mandatory')
ibmtn3270eConnRejectAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmtn3270eConnRejectAddrType.setStatus('mandatory')
ibmtn3270eConnRejectClient = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmtn3270eConnRejectClient.setStatus('mandatory')
ibmtn3270eConnRejectReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44))).clone(namedValues=NamedValues(("noportinfo", 1), ("cliunknown", 2), ("clinoauth", 3), ("sockblock", 4), ("nodeterm", 5), ("createfail", 6), ("seqnum", 7), ("negfailed", 8), ("notelquale", 9), ("termtypefail", 10), ("notypeprtgen", 11), ("clirplyfail", 12), ("valtelquale", 13), ("clisendfail", 14), ("failtelquale", 15), ("termtypagain", 16), ("noportagain", 17), ("prtnoluname", 18), ("clinoauthent", 19), ("clinoauthflt", 20), ("noluconf", 21), ("noportmore", 22), ("noresource", 23), ("nameresource", 24), ("prtnoluagain", 25), ("noimplu", 26), ("lunotfound", 27), ("valluprt", 28), ("vallu", 29), ("prtlunofind", 30), ("nameinuse", 31), ("reqlunofind", 32), ("valprtagain", 33), ("valluagain", 34), ("luprtnofind", 35), ("poolluinuse", 36), ("poollunofind", 37), ("restypnofind", 38), ("poolluconf", 39), ("lucapreach", 40), ("noappnmem", 41), ("nomoreconn", 42), ("pooldep", 43), ("termnorsp", 44)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmtn3270eConnRejectReason.setStatus('mandatory')
ibmtn3270eConnRejectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmtn3270eConnRejectTime.setStatus('mandatory')
mibBuilder.exportSymbols("IBM-TN3270E-MIB", ibmtn3270eConnRejectClient=ibmtn3270eConnRejectClient, ibmtn3270eConnRejectAddrType=ibmtn3270eConnRejectAddrType, ibmtn3270eConnRejectTime=ibmtn3270eConnRejectTime, ibmtn3270eConnRejectIndex=ibmtn3270eConnRejectIndex, ibmtn3270eConnRejectReason=ibmtn3270eConnRejectReason, ibmtn3270eConnRejectEntry=ibmtn3270eConnRejectEntry, ibmtn3270eMIB=ibmtn3270eMIB, ibmtn3270eConnRejectTable=ibmtn3270eConnRejectTable)
