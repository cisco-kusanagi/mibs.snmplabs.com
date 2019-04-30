#
# PySNMP MIB module AIDIALOUT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AIDIALOUT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:00:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, enterprises, Counter64, ObjectIdentity, Bits, Counter32, TimeTicks, Integer32, Unsigned32, NotificationType, IpAddress, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "Counter64", "ObjectIdentity", "Bits", "Counter32", "TimeTicks", "Integer32", "Unsigned32", "NotificationType", "IpAddress", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiDialOut = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 36))
if mibBuilder.loadTexts: aiDialOut.setLastUpdated('9909151700Z')
if mibBuilder.loadTexts: aiDialOut.setOrganization('Applied Innovation Inc.')
aiDialOutTable = MibTable((1, 3, 6, 1, 4, 1, 539, 36, 1), )
if mibBuilder.loadTexts: aiDialOutTable.setStatus('current')
aiDialOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 36, 1, 1), ).setIndexNames((0, "AIDIALOUT-MIB", "aiDialOutLinkNumber"))
if mibBuilder.loadTexts: aiDialOutEntry.setStatus('current')
aiDialOutLinkNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiDialOutLinkNumber.setStatus('current')
aiDialOutStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiDialOutStatus.setStatus('current')
aiDialOutPrimaryDialString = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiDialOutPrimaryDialString.setStatus('current')
aiDialOutSecondaryDialString = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiDialOutSecondaryDialString.setStatus('current')
aiDialOutTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 300))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiDialOutTimeOut.setStatus('current')
aiDialOutAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiDialOutAttempts.setStatus('current')
aiDialOutInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 36, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiDialOutInterval.setStatus('current')
mibBuilder.exportSymbols("AIDIALOUT-MIB", aiDialOut=aiDialOut, aiDialOutPrimaryDialString=aiDialOutPrimaryDialString, aiDialOutStatus=aiDialOutStatus, aiDialOutTable=aiDialOutTable, PYSNMP_MODULE_ID=aiDialOut, aiDialOutLinkNumber=aiDialOutLinkNumber, aii=aii, aiDialOutSecondaryDialString=aiDialOutSecondaryDialString, aiDialOutTimeOut=aiDialOutTimeOut, aiDialOutEntry=aiDialOutEntry, aiDialOutInterval=aiDialOutInterval, PositiveInteger=PositiveInteger, aiDialOutAttempts=aiDialOutAttempts)
