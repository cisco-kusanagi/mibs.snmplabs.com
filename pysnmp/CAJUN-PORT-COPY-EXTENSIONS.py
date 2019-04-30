#
# PySNMP MIB module CAJUN-PORT-COPY-EXTENSIONS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CAJUN-PORT-COPY-EXTENSIONS
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
lsg, = mibBuilder.importSymbols("AVAYAGEN-MIB", "lsg")
portCopyEntry, = mibBuilder.importSymbols("SMON-MIB", "portCopyEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Counter64, ObjectIdentity, MibIdentifier, Gauge32, NotificationType, iso, Unsigned32, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Counter64", "ObjectIdentity", "MibIdentifier", "Gauge32", "NotificationType", "iso", "Unsigned32", "Counter32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

cjnPortCopyExtensions = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 2, 1, 5))
if mibBuilder.loadTexts: cjnPortCopyExtensions.setLastUpdated('0105290000Z')
if mibBuilder.loadTexts: cjnPortCopyExtensions.setOrganization("Avaya's Concord Technology Center (CTC)")
cjnPortCopyTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1), )
if mibBuilder.loadTexts: cjnPortCopyTable.setStatus('current')
cjnPortCopyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1), )
portCopyEntry.registerAugmentions(("CAJUN-PORT-COPY-EXTENSIONS", "cjnPortCopyEntry"))
cjnPortCopyEntry.setIndexNames(*portCopyEntry.getIndexNames())
if mibBuilder.loadTexts: cjnPortCopyEntry.setStatus('current')
cjnPortCopyChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnPortCopyChannel.setStatus('current')
cjnPortCopySamplingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("always", 1), ("periodic", 2))).clone('always')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnPortCopySamplingMode.setStatus('current')
cjnPortCopyMaxPacketsPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnPortCopyMaxPacketsPerSecond.setStatus('current')
cjnPortCopySAFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1, 4), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnPortCopySAFilter.setStatus('current')
cjnPortCopyDAFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1, 5), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnPortCopyDAFilter.setStatus('current')
cjnPortCopyFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("sa", 1), ("da", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnPortCopyFilter.setStatus('current')
mibBuilder.exportSymbols("CAJUN-PORT-COPY-EXTENSIONS", cjnPortCopySamplingMode=cjnPortCopySamplingMode, cjnPortCopyDAFilter=cjnPortCopyDAFilter, MacAddress=MacAddress, cjnPortCopyMaxPacketsPerSecond=cjnPortCopyMaxPacketsPerSecond, cjnPortCopyChannel=cjnPortCopyChannel, cjnPortCopySAFilter=cjnPortCopySAFilter, cjnPortCopyEntry=cjnPortCopyEntry, PYSNMP_MODULE_ID=cjnPortCopyExtensions, cjnPortCopyFilter=cjnPortCopyFilter, cjnPortCopyTable=cjnPortCopyTable, cjnPortCopyExtensions=cjnPortCopyExtensions)
