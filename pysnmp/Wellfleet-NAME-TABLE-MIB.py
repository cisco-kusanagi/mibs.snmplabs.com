#
# PySNMP MIB module Wellfleet-NAME-TABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-NAME-TABLE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:34:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, NotificationType, ObjectIdentity, TimeTicks, MibIdentifier, IpAddress, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "NotificationType", "ObjectIdentity", "TimeTicks", "MibIdentifier", "IpAddress", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfName, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfName")
wfNameEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 18, 1))
wfNameDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 18, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNameDelete.setStatus('mandatory')
wfNameName = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 18, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNameName.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-NAME-TABLE-MIB", wfNameName=wfNameName, wfNameEntry=wfNameEntry, wfNameDelete=wfNameDelete)
