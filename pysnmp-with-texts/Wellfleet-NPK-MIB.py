#
# PySNMP MIB module Wellfleet-NPK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-NPK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:41:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, NotificationType, ModuleIdentity, Unsigned32, MibIdentifier, iso, TimeTicks, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "NotificationType", "ModuleIdentity", "Unsigned32", "MibIdentifier", "iso", "TimeTicks", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfGameGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfGameGroup")
wfNpkBase = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 8))
wfNpkBaseCreate = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNpkBaseCreate.setStatus('mandatory')
if mibBuilder.loadTexts: wfNpkBaseCreate.setDescription('Create/Delete parameter')
wfNpkBaseHash = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 8, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNpkBaseHash.setStatus('mandatory')
if mibBuilder.loadTexts: wfNpkBaseHash.setDescription('Hash value: MD5 of NPK used to protect this configuration')
wfNpkBaseLastMod = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 8, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNpkBaseLastMod.setStatus('mandatory')
if mibBuilder.loadTexts: wfNpkBaseLastMod.setDescription('Stores Last modification time-stamp for NPK')
mibBuilder.exportSymbols("Wellfleet-NPK-MIB", wfNpkBase=wfNpkBase, wfNpkBaseCreate=wfNpkBaseCreate, wfNpkBaseLastMod=wfNpkBaseLastMod, wfNpkBaseHash=wfNpkBaseHash)
