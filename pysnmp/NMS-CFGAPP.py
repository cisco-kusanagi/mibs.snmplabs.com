#
# PySNMP MIB module NMS-CFGAPP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-CFGAPP
# Produced by pysmi-0.3.4 at Mon Apr 29 20:11:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
nmstemporary, = mibBuilder.importSymbols("NMS-SMI", "nmstemporary")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, MibIdentifier, Counter64, TimeTicks, NotificationType, Unsigned32, Gauge32, IpAddress, Bits, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "MibIdentifier", "Counter64", "TimeTicks", "NotificationType", "Unsigned32", "Gauge32", "IpAddress", "Bits", "iso", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nmscfgapp = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 3, 8))
nmsCfgAddToBuf = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 3, 8, 1), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmsCfgAddToBuf.setStatus('mandatory')
nmsCfgAppAction = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 3, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("apply", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmsCfgAppAction.setStatus('mandatory')
nmsCfgClearBuf = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 3, 8, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmsCfgClearBuf.setStatus('mandatory')
nmsCfgAppResult = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 3, 8, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsCfgAppResult.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-CFGAPP", nmsCfgAppResult=nmsCfgAppResult, nmsCfgAppAction=nmsCfgAppAction, nmsCfgClearBuf=nmsCfgClearBuf, nmsCfgAddToBuf=nmsCfgAddToBuf, nmscfgapp=nmscfgapp)
