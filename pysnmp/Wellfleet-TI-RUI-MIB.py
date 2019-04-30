#
# PySNMP MIB module Wellfleet-TI-RUI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-TI-RUI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:35:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, Bits, Gauge32, Integer32, Unsigned32, Counter64, IpAddress, NotificationType, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "Bits", "Gauge32", "Integer32", "Unsigned32", "Counter64", "IpAddress", "NotificationType", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfServices, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfServices")
wfTiRui = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2))
wfTiRuiState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTiRuiState.setStatus('mandatory')
wfTiRuiAction = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTiRuiAction.setStatus('mandatory')
wfTiRuiResult = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTiRuiResult.setStatus('mandatory')
wfTiRuiInReqs = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTiRuiInReqs.setStatus('mandatory')
wfTiRuiOutResults = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTiRuiOutResults.setStatus('mandatory')
wfTiRuiOutResultsErr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTiRuiOutResultsErr.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-TI-RUI-MIB", wfTiRuiInReqs=wfTiRuiInReqs, wfTiRuiResult=wfTiRuiResult, wfTiRuiState=wfTiRuiState, wfTiRuiOutResultsErr=wfTiRuiOutResultsErr, wfTiRui=wfTiRui, wfTiRuiOutResults=wfTiRuiOutResults, wfTiRuiAction=wfTiRuiAction)
