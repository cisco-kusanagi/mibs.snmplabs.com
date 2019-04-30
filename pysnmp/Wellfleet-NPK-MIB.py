#
# PySNMP MIB module Wellfleet-NPK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-NPK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:34:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Gauge32, Bits, Counter32, NotificationType, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, TimeTicks, ModuleIdentity, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "Bits", "Counter32", "NotificationType", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "TimeTicks", "ModuleIdentity", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfGameGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfGameGroup")
wfNpkBase = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 8))
wfNpkBaseCreate = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNpkBaseCreate.setStatus('mandatory')
wfNpkBaseHash = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 8, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNpkBaseHash.setStatus('mandatory')
wfNpkBaseLastMod = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 8, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNpkBaseLastMod.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-NPK-MIB", wfNpkBase=wfNpkBase, wfNpkBaseHash=wfNpkBaseHash, wfNpkBaseLastMod=wfNpkBaseLastMod, wfNpkBaseCreate=wfNpkBaseCreate)
