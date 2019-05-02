#
# PySNMP MIB module NMS-CFGAPP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-CFGAPP
# Produced by pysmi-0.3.4 at Wed May  1 14:21:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
nmstemporary, = mibBuilder.importSymbols("NMS-SMI", "nmstemporary")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, Counter64, IpAddress, ModuleIdentity, ObjectIdentity, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Counter64", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nmscfgapp = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 3, 8))
nmsCfgAddToBuf = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 3, 8, 1), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmsCfgAddToBuf.setStatus('mandatory')
if mibBuilder.loadTexts: nmsCfgAddToBuf.setDescription('add command to buffer')
nmsCfgAppAction = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 3, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("apply", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmsCfgAppAction.setStatus('mandatory')
if mibBuilder.loadTexts: nmsCfgAppAction.setDescription('apply commands')
nmsCfgClearBuf = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 3, 8, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmsCfgClearBuf.setStatus('mandatory')
if mibBuilder.loadTexts: nmsCfgClearBuf.setDescription('clear command-buffer')
nmsCfgAppResult = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 3, 8, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsCfgAppResult.setStatus('mandatory')
if mibBuilder.loadTexts: nmsCfgAppResult.setDescription('the result of application')
mibBuilder.exportSymbols("NMS-CFGAPP", nmsCfgClearBuf=nmsCfgClearBuf, nmsCfgAppResult=nmsCfgAppResult, nmsCfgAppAction=nmsCfgAppAction, nmscfgapp=nmscfgapp, nmsCfgAddToBuf=nmsCfgAddToBuf)
