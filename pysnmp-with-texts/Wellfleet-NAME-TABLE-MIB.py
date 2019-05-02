#
# PySNMP MIB module Wellfleet-NAME-TABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-NAME-TABLE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:41:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, Integer32, TimeTicks, Counter32, ObjectIdentity, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Unsigned32, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Integer32", "TimeTicks", "Counter32", "ObjectIdentity", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Unsigned32", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfName, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfName")
wfNameEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 18, 1))
wfNameDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 18, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNameDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfNameDelete.setDescription('Create or Delete the Object Base Record')
wfNameName = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 18, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNameName.setStatus('mandatory')
if mibBuilder.loadTexts: wfNameName.setDescription('The BCC name of an object')
mibBuilder.exportSymbols("Wellfleet-NAME-TABLE-MIB", wfNameEntry=wfNameEntry, wfNameName=wfNameName, wfNameDelete=wfNameDelete)
