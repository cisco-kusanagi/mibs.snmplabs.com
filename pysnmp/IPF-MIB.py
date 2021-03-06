#
# PySNMP MIB module IPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:44:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, Unsigned32, MibIdentifier, Gauge32, Integer32, IpAddress, ModuleIdentity, enterprises, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Unsigned32", "MibIdentifier", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "enterprises", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sbe = MibIdentifier((1, 3, 6, 1, 4, 1, 1055))
ipf = MibIdentifier((1, 3, 6, 1, 4, 1, 1055, 5))
ipfMIBVersion = MibScalar((1, 3, 6, 1, 4, 1, 1055, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfMIBVersion.setStatus('mandatory')
ipfVersion = MibScalar((1, 3, 6, 1, 4, 1, 1055, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfVersion.setStatus('mandatory')
ipfState = MibScalar((1, 3, 6, 1, 4, 1, 1055, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfState.setStatus('mandatory')
ipfCommand = MibScalar((1, 3, 6, 1, 4, 1, 1055, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("update", 1), ("disable", 2), ("enable", 3), ("delete", 4), ("clear", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfCommand.setStatus('mandatory')
ipfDefAction = MibScalar((1, 3, 6, 1, 4, 1, 1055, 5, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("block", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfDefAction.setStatus('mandatory')
ipfParseTable = MibTable((1, 3, 6, 1, 4, 1, 1055, 5, 6), )
if mibBuilder.loadTexts: ipfParseTable.setStatus('mandatory')
ipfParseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1055, 5, 6, 2), ).setIndexNames((0, "IPF-MIB", "ipfParseEntryNumber"))
if mibBuilder.loadTexts: ipfParseEntry.setStatus('mandatory')
ipfParseEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 6, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("valid", 1), ("create-request", 2), ("under-creation", 3), ("invalid", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfParseEntryStatus.setStatus('mandatory')
ipfParseEntryNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 6, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfParseEntryNumber.setStatus('mandatory')
ipfParseEntryText = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 6, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfParseEntryText.setStatus('mandatory')
ipfParseEntryError = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 6, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfParseEntryError.setStatus('mandatory')
ipfCurrRules = MibTable((1, 3, 6, 1, 4, 1, 1055, 5, 7), )
if mibBuilder.loadTexts: ipfCurrRules.setStatus('mandatory')
ipfCurrRule = MibTableRow((1, 3, 6, 1, 4, 1, 1055, 5, 7, 2), ).setIndexNames((0, "IPF-MIB", "ipfCurrRuleNumber"))
if mibBuilder.loadTexts: ipfCurrRule.setStatus('mandatory')
ipfCurrRuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("valid", 1), ("create-request", 2), ("under-creation", 3), ("invalid", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfCurrRuleStatus.setStatus('mandatory')
ipfCurrRuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 7, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfCurrRuleNumber.setStatus('mandatory')
ipfCurrRuleText = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 7, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfCurrRuleText.setStatus('mandatory')
ipfCurrRuleFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 7, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfCurrRuleFlags.setStatus('mandatory')
ipfCurrRuleHits = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 7, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfCurrRuleHits.setStatus('mandatory')
ipfCurrRuleBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 7, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfCurrRuleBytes.setStatus('mandatory')
natCurrRules = MibTable((1, 3, 6, 1, 4, 1, 1055, 5, 8), )
if mibBuilder.loadTexts: natCurrRules.setStatus('mandatory')
natCurrRule = MibTableRow((1, 3, 6, 1, 4, 1, 1055, 5, 8, 2), ).setIndexNames((0, "IPF-MIB", "natCurrRuleNumber"))
if mibBuilder.loadTexts: natCurrRule.setStatus('mandatory')
natCurrRuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 8, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("valid", 1), ("create-request", 2), ("under-creation", 3), ("invalid", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: natCurrRuleStatus.setStatus('mandatory')
natCurrRuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 8, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natCurrRuleNumber.setStatus('mandatory')
natCurrRuleText = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 8, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: natCurrRuleText.setStatus('mandatory')
natCurrRuleHits = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 8, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natCurrRuleHits.setStatus('mandatory')
natCurrRulePend = MibTableColumn((1, 3, 6, 1, 4, 1, 1055, 5, 8, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natCurrRulePend.setStatus('mandatory')
mibBuilder.exportSymbols("IPF-MIB", ipfParseEntryError=ipfParseEntryError, natCurrRuleText=natCurrRuleText, natCurrRules=natCurrRules, ipfParseEntry=ipfParseEntry, ipfParseEntryText=ipfParseEntryText, sbe=sbe, natCurrRuleHits=natCurrRuleHits, ipfParseTable=ipfParseTable, ipfParseEntryNumber=ipfParseEntryNumber, ipfCurrRules=ipfCurrRules, ipfCurrRule=ipfCurrRule, natCurrRule=natCurrRule, ipfMIBVersion=ipfMIBVersion, ipfCurrRuleNumber=ipfCurrRuleNumber, ipf=ipf, ipfCommand=ipfCommand, ipfCurrRuleBytes=ipfCurrRuleBytes, ipfCurrRuleStatus=ipfCurrRuleStatus, ipfState=ipfState, ipfCurrRuleHits=ipfCurrRuleHits, ipfDefAction=ipfDefAction, ipfVersion=ipfVersion, natCurrRuleStatus=natCurrRuleStatus, natCurrRulePend=natCurrRulePend, ipfCurrRuleText=ipfCurrRuleText, natCurrRuleNumber=natCurrRuleNumber, ipfCurrRuleFlags=ipfCurrRuleFlags, ipfParseEntryStatus=ipfParseEntryStatus)
